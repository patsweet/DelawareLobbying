# Functions to parse the xml strings that the state pushed into the
# Excel spreadsheets.
import Lobbyists
import PublicOfficers
import xml.etree.ElementTree as ET

def parseLobbyistXML(xml_string):
    """
        Parses the XML strings in the Lobbying disclosures and
        returns a list of Lobbyists.Expenditure objects and
        Lobbyists.Gift objects.
    """
    expenditures = []
    gifts = []
    root = ET.fromstring(xml_string)
    lobs_employer_expenditures = root.findall('.//LobsEmployerExpenditure')
    lobs_po_gifts = root.findall('.//LobsPOGifts')
    # Parse expenditures from lee
    for expenditure in lobs_employer_expenditures:
        x = Lobbyists.Expenditure(
            expenditure.find('ItemId').text,
            expenditure.find('DisclosureId').text,
            Lobbyists.Employer(
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
        g = Lobbyists.Gift(
            gift.find('ItemId').text,
            gift.find('DisclosureId').text,
            Lobbyists.Employer(
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

def parsePublicOfficerXML(xml_string):
    pass