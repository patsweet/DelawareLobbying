##############################################################################
#     ____        __         ____  _________
#    / __ \__  __/ /_       / __ \/ __/ __(_)_______  __________
#   / /_/ / / / / __ \     / / / / /_/ /_/ / ___/ _ \/ ___/ ___/
#  / ____/ /_/ / /_/ /    / /_/ / __/ __/ / /__/  __/ /  (__  )
# /_/    \__,_/_.___(_)   \____/_/ /_/ /_/\___/\___/_/  /____/
#
# Models for the disclosures from Public Officers.
#   - PublicOfficer objects include lists of all the classes above it.
##############################################################################


class InstrumentOwnership(object):
    """docstring for InstrumentOwnership"""
    def __init__(self, item_id, disclosure_id, name, instrument,
        nature_of_ownership):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.name = name
        self.instrument = instrument
        self.nature_of_ownership = nature_of_ownership


class BusinessEnterprise(object):
    """docstring for BusinessEnterprise"""
    def __init__(self, item_id, disclosure_id, name, name_of_ownership,
        position_of_management):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.name = name
        self.name_of_ownership = name_of_ownership
        self.position_of_management = position_of_management


class ProfessionalOrganization(object):
     """docstring for ProfessionalOrganization"""
     def __init__(self, item_id, disclosure_id, organization_name,
        address, type_of_practice, management_position):
         self.item_id = item_id
         self.disclosure_id = disclosure_id
         self.organization_name = organization_name
         self.address = address
         self.type_of_practice = type_of_practice
         self.management_position = management_position


class ConstructiveControl(object):
    """docstring for ConstructiveControl"""
    def __init__(self, item_id, disclosure_id, entity_name, entity_instrument,
        nature_of_constrol):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.entity_name = entity_name
        self.entity_instrument = entity_instrument
        self.nature_of_constrol = nature_of_constrol


class Creditor(object):
    """docstring for Creditor"""
    def __init__(self, item_id, disclosure_id, creditor_name):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.creditor_name = creditor_name


class IncomeService(object):
    """docstring for IncomeService"""
    def __init__(self, item_id, disclosure_id, income_source_type_id,
        income_source_type, income_source):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.income_source_type_id = income_source_type_id
        self.income_source_type = income_source_type
        self.income_source = income_source


class CapitalGain(object):
    """docstring for CapitalGain"""
    def __init__(self, item_id, disclosure_id, capital_gain_name):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.capital_gain_name = capital_gain_name


class ReimbursedExpenditure(object):
    """docstring for ReimbursedExpenditure"""
    def __init__(self, item_id, disclosure_id, expenditure_source):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.expenditure_source = expenditure_source


class Honoraria(object):
    """docstring for Honoraria"""
    def __init__(self, item_id, disclosure_id, honoraria_source):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.honoraria_source = honoraria_source


class Gift(object):
    """docstring for Gift"""
    def __init__(self, item_id, disclosure_id, gift_type_id, gift_type,
        gift_source, gift_value):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.gift_type_id = gift_type_id
        self.gift_type = gift_type
        self.gift_source = gift_source
        self.gift_value = gift_value


class IncomeSource(object):
    """
        Income source (IncomeSourceCollection) appears to be
        blank for all Public Officers of the state. Not used?
    """
    pass


class BoardMembership(object):
    """docstring for BoardMembership"""
    def __init__(self, item_id, disclosure_id, membership_type_id,
        membership_type, membership_name, membership_address):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.membership_type_id = membership_type_id
        self.membership_type = membership_type
        self.membership_name = membership_name
        self.membership_address = membership_address


class PublicOfficer(object):
    """An employee of the state"""
    def __init__(self, first_name, middle_name, last_name, state_position,
        submitted_date, year, instrument_ownership, business_enterprise,
        pro_organization, constructive_control, creditor, income_service,
        capital_gain, reimbursed_expenditures, honoraria, gifts,
        source_of_income, board_membership):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.state_position = state_position
        self.submitted_date = submitted_date
        self.year = year
        self.instrument_ownership = instrument_ownership
        self.business_enterprise = business_enterprise
        self.pro_organization = pro_organization
        self.constructive_control = constructive_control
        self.creditor = creditor
        self.income_service = income_service
        self.capital_gain = capital_gain
        self.reimbursed_expenditures = reimbursed_expenditures
        self.honoraria = honoraria
        self.gifts = gifts
        self.source_of_income = source_of_income
        self.board_membership = board_membership
