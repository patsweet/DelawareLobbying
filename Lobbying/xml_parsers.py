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
    # Parse expenditures from lobs_employer_expenditures
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
    # Parse gifts from lobs_po_gifts
    for gift in lobs_po_gifts:
        try:
            employer = Lobbyists.Employer(
                gift.find('Employer/EmployerId').text,
                gift.find('Employer/LegalName').text,
                gift.find('Employer/AddressLine1').text,
                gift.find('Employer/AddressLine2').text,
                gift.find('Employer/City').text,
                gift.find('Employer/State').text,
                gift.find('Employer/ZipCode').text
            )
        except AttributeError, e:
            employer = None
        g = Lobbyists.Gift(
            gift.find('ItemId').text,
            gift.find('DisclosureId').text,
            employer,
            gift.find('GiftDate').text[:10],
            gift.find('POId').text,
            gift.find('POName').text,
            gift.find('GiftDescription').text,
            gift.find('GiftValue').text
        )
        gifts.append(g)
    return expenditures, gifts


def parsePublicOfficerXML(xml_string):
    """
    Parses the xml string for seven collections of data
    that we'll return in a dictionary of lists.
    """
    xml_data = {
        "instrument_ownership": [], "business_enterprise": [],
        "pro_organization": [], "constructive_control": [], "creditor": [],
        "income_service": [], "capital_gain": [],
        "reimbursed_expenditures": [], "honoraria": [], "gifts": [],
        "source_of_income": [], "board_membership": []
    }
    root = ET.fromstring(xml_string)
    # Instrument ownership
    for instrument in root.findall(".//POQ_InstrumentOwnership"):
        xml_data["instrument_ownership"].append(
            PublicOfficers.InstrumentOwnership(
                item_id=instrument.find("ItemId").text,
                disclosure_id=instrument.find("DisclosureId").text,
                name=instrument.find("Name").text,
                instrument=instrument.find("Instrument").text,
                nature_of_ownership=instrument.find("NatureOfOwnership").text
            )
        )
    # Business Enterprises
    for business in root.findall(".//POQ_BusinessEnterprise"):
        xml_data["business_enterprise"].append(
            PublicOfficers.BusinessEnterprise(
                item_id=business.find("ItemId").text,
                disclosure_id=business.find("DisclosureId").text,
                name=business.find("Name").text,
                name_of_ownership=business.find("NameOfOwnership").text,
                position_of_management=business.find("PositionOfManagement").text
            )
        )
    # Professional Organizations
    for org in root.findall(".//POQ_ProfessionalOrganisation"):
        xml_data["pro_organization"].append(
            PublicOfficers.ProfessionalOrganization(
                item_id=org.find("ItemId").text,
                disclosure_id=org.find("DisclosureId").text,
                organization_name=org.find("OrganizationName").text,
                address=org.find("Address").text,
                type_of_practice=org.find("TypeofPractice").text,
                management_position=org.find("ManagementPosition").text
            )
        )
    # Constructive Controls
    for control in root.findall(".//POQ_ConstructiveControl"):
        xml_data["constructive_control"].append(
            PublicOfficers.ConstructiveControl(
                item_id=control.find("ItemId").text,
                disclosure_id=control.find("DisclosureId").text,
                entity_name=control.find("EntityName").text,
                entity_instrument=control.find("EntityInstrument").text,
                nature_of_control=control.find("NatureofControl").text
            )
        )
    # Creditors
    for creditor in root.findall(".//POQ_Creditor"):
        xml_data["creditor"].append(
            PublicOfficers.Creditor(
                item_id=creditor.find("ItemId").text,
                disclosure_id=creditor.find("DisclosureId").text,
                creditor_name=creditor.find("CreditorName").text
            )
        )
    # Income Services
    for service in root.findall(".//POQ_IncomeService"):
        xml_data["income_service"].append(
            PublicOfficers.IncomeService(
                item_id=service.find("ItemId").text,
                disclosure_id=service.find("DisclosureId").text,
                income_source_type_id=service.find("IncomesourceTypeId").text,
                income_source_type=service.find("IncomesourceType").text,
                income_source=service.find("IncomeSource").text
            )
        )
    # Capital Gains
    for gain in root.findall(".//POQ_CapitalGain"):
        xml_data["capital_gain"].append(
            PublicOfficers.CapitalGain(
                item_id=gain.find("ItemId").text,
                disclosure_id=gain.find("DisclosureId").text,
                capital_gain_name=gain.find("CapitalGainName").text
            )
        )
    # Reimbursed Expenditures
    for expenditure in root.findall(".//POQ_ReimburseExpenditure"):
        xml_data["reimbursed_expenditures"].append(
            PublicOfficers.ReimbursedExpenditure(
                item_id=expenditure.find("ItemId").text,
                disclosure_id=expenditure.find("DisclosureId").text,
                expenditure_source=expenditure.find("ExpenditureSource").text
            )
        )
    # honoraria
    for honor in root.findall(".//POQ_Honoraria"):
        xml_data["honoraria"].append(
            PublicOfficers.Honoraria(
                item_id=honor.find("ItemId").text,
                disclosure_id=honor.find("DisclosureId").text,
                honoraria_source=honor.find("HonorariaSource").text
            )
        )
    # gifts
    for gift in root.findall(".//POQ_Gift"):
        xml_data["gifts"].append(
            PublicOfficers.Gift(
                item_id=gift.find("ItemId").text,
                disclosure_id=gift.find("DisclosureId").text,
                gift_type_id=gift.find("GiftTypeId").text,
                gift_type=gift.find("GiftType").text,
                gift_source=gift.find("GiftSource").text,
                gift_value=gift.find("GiftValue").text
            )
        )
    # source_of_income
    # This doesn't appear to be used at all.
    for source in root.findall(".//POQ_SourceOfIncome"):
        pass
    # board_membership
    for board in root.findall(".//POQ_BoardMembership"):
        xml_data["board_membership"].append(
            PublicOfficers.BoardMembership(
                item_id=board.find("ItemId").text,
                disclosure_id=board.find("DisclosureId").text,
                membership_type_id=board.find("MembershipTypeId").text,
                membership_type=board.find("MembershipType").text,
                membership_name=board.find("MembershipName").text,
                membership_address=board.find("MembershipAddress").text
            )
        )
    return xml_data
