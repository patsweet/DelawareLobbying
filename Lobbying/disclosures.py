##############################################################################
# Main script to parse and output public lobbying disclosures.
##############################################################################

import os
import csv
import json
from xml_parsers import parseLobbyistXML
from Lobbyists import Employer, Expenditure, Gift, Lobbyist
from settings import BASE_DIR, IFILE, JSONOUT, GIFTSOUT, EXPENDOUT


class LobbyistEncoder(json.JSONEncoder):
    """
        Helper class to translate classes in Lobbyists to
        JSON.
    """
    def default(self, obj):
        if not isinstance(obj, Lobbyist) \
        and not isinstance(obj, Employer) \
        and not isinstance(obj, Expenditure) \
        and not isinstance(obj, Gift):
            return super(MyEncoder, self).default(obj)
        return obj.__dict__


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
        'last_name', 'first_name', 'year', 'quarter', 'employer',
        'employer_id', 'food_refreshments', 'entertainment', 'lodging',
        'travel', 'recreation', 'gifts'
    ]
    with open(EXPENDOUT, 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for lobbyist in lobbyists:
            for expenditure in lobbyist.expenditures:
                out = [
                    lobbyist.last_name,
                    lobbyist.first_name,
                    lobbyist.year,
                    lobbyist.quarter,
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
    with open(IFILE, 'r') as csvfile, open(JSONOUT, 'w+') as jsonfile:
        record_id = 1
        reader = csv.reader(csvfile, delimiter='|')
        reader.next()  # Skip the first row
        for row in reader:
            row = [item.decode('iso-8859-1').encode('utf8') for item in row]
            expenditures, gifts = parseLobbyistXML(row[8])  # Must parse xml string.
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
        jsonfile.write(json.dumps(lobbyists, cls=LobbyistEncoder, sort_keys=True,
            indent=4, separators=(',', ': ')))
    # Generate the pipe-delimited files
    generateGifts(lobbyists)
    generateExpendetures(lobbyists)

if __name__ == '__main__':
    main()
