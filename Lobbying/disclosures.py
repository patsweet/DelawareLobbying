import os
import csv
import json
import xml.etree.ElementTree as ET
from Lobbyists import Employer, Expenditure, Gift, Lobbyist

# CONSTANTS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IFILE = os.path.join(BASE_DIR, "Lobbyist database 2013.csv")
OFILE = os.path.join(BASE_DIR, "lobbyists.json")
GIFTSOUT = os.path.join(BASE_DIR, "lobbyist_gifts.txt")
EXPENDOUT = os.path.join(BASE_DIR, "lobbyist_expenditures.txt")

class MyEncoder(json.JSONEncoder):
    """Takes a class and turns it into a json string"""
    def default(self, obj):
        if not isinstance(obj, Lobbyist) \
        and not isinstance(obj, Employer) \
        and not isinstance(obj, Expenditure) \
        and not isinstance(obj, Gift):
            return super(MyEncoder, self).default(obj)
        return obj.__dict__


def parseXML(xml_string):
    """
    Parses the xml string and returns an array of Disclosure and Employer
    objects.
    """
    expenditures = []
    gifts = []
    root = ET.fromstring(xml_string)
    lobs_employer_expenditures = root.findall('.//LobsEmployerExpenditure')
    lobs_po_gifts = root.findall('.//LobsPOGifts')
    # Parse expenditures from lee
    for expenditure in lobs_employer_expenditures:
        x = Expenditure(
            expenditure.find('ItemId').text,
            expenditure.find('DisclosureId').text,
            Employer(
                expenditure.find('Employer/EmployerId').text,
                expenditure.find('Employer/LegalName').text,
                expenditure.find('Employer/AddressLine1').text,
                expenditure.find('Employer/AddressLine2').text,
                expenditure.find('Employer/City').text,
                expenditure.find('Employer/State').text,
                expenditure.find('Employer/ZipCode').text
            ),
            expenditure.find('EmployerId').text,
            float(expenditure.find('FoodRefreshments').text),
            float(expenditure.find('Entertainment').text),
            float(expenditure.find('LodgingExpenses').text),
            float(expenditure.find('TravelExpense').text),
            float(expenditure.find('RecreationExpense').text),
            float(expenditure.find('GiftContributions').text)
        )
        expenditures.append(x)
    # Parse gifts from lpg
    for gift in lobs_po_gifts:
        g = Gift(
            gift.find('ItemId').text,
            gift.find('DisclosureId').text,
            Employer(
                gift.find('Employer/EmployerId').text,
                gift.find('Employer/LegalName').text,
                gift.find('Employer/AddressLine1').text,
                gift.find('Employer/AddressLine2').text,
                gift.find('Employer/City').text,
                gift.find('Employer/State').text,
                gift.find('Employer/ZipCode').text
            ),
            gift.find('GiftDate').text[:10],
            gift.find('POId').text,
            gift.find('POName').text,
            gift.find('GiftDescription').text,
            gift.find('GiftValue').text
        )
        gifts.append(g)
    return expenditures, gifts

def generateGifts(lobbyists):
    header = [
        'last_name', 'first_name', 'employer', 'legislator',
        'gift_date', 'gift_description', 'gift_value'
    ]
    with open(GIFTSOUT, 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for lobbyist in lobbyists:
            for gift in lobbyist.gifts:
                out = [
                    lobbyist.last_name,
                    lobbyist.first_name,
                    gift.employer.legal_name,
                    gift.poname,
                    gift.gift_date,
                    gift.gift_description,
                    gift.gift_value
                ]
                ofile.write("|".join(out) + "\n")

def generateExpendetures(lobbyists):
    header = [
        'last_name', 'first_name', 'employer', 'employer_id',
        'food_refreshments', 'entertainment', 'lodging', 'travel',
        'recreation', 'gifts'
    ]
    with open(EXPENDOUT, 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for lobbyist in lobbyists:
            for expenditure in lobbyist.expenditures:
                out = [
                    lobbyist.last_name,
                    lobbyist.first_name,
                    expenditure.employer.legal_name,
                    expenditure.employer.employer_id,
                    expenditure.food_refreshments,
                    expenditure.lodging_expenses,
                    expenditure.travel_expenses,
                    expenditure.recreation_expenses,
                    expenditure.gift_contributions
                ]
                out = [str(item) for item in out]
                ofile.write("|".join(out) + "\n")


def main():
    """
    Parse the csv file and create a master json file
    and pipe-delimited files for gifts and expenditures.
    """
    lobbyists = []
    with open(IFILE, 'r') as csvfile, open(OFILE, 'w+') as jsonfile:
        record_id = 1
        reader = csv.reader(csvfile, delimiter='|')
        reader.next()  # Skip the first row
        for row in reader:
            row = [item.decode('iso-8859-1').encode('utf8') for item in row]
            expenditures, gifts = parseXML(row[8])  # Must parse xml string.
            lobbyist = Lobbyist(
                record_id,
                row[0],  # first name
                row[1],  # last name
                row[2],  # occupation
                row[3],  # lobbyist only
                row[4],  # employment explain
                row[5],  # submit date
                row[6],  # year
                row[7],  # quarter
                expenditures,
                gifts
            )
            record_id += 1
            lobbyists.append(lobbyist)
        jsonfile.write(json.dumps(lobbyists, cls=MyEncoder, sort_keys=True,
            indent=4, separators=(',', ': ')))
    # Generate the pipe-delimited files
    generateGifts(lobbyists)
    generateExpendetures(lobbyists)

if __name__ == '__main__':
    main()
