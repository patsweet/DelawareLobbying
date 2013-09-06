##############################################################################
#     ____        __         ____  _________
#    / __ \__  __/ /_       / __ \/ __/ __(_)_______  __________
#   / /_/ / / / / __ \     / / / / /_/ /_/ / ___/ _ \/ ___/ ___/
#  / ____/ /_/ / /_/ /    / /_/ / __/ __/ / /__/  __/ /  (__  )
# /_/    \__,_/_.___(_)   \____/_/ /_/ /_/\___/\___/_/  /____/
#
# Models for the disclosures from Public Officers.
#   - PublicOfficer
#       - first name (string)
#       - middle name (string)
#       - last name (string)
#       - state position (string)
#       - submitted date (datetime)
#       - year (string)
#       - instrument ownerships (list of objects)
#       - business enterprises (list of objects)
#       - professional organization (list of objects)
#       - constructive control (list of objects)
#       - creditor (list of objects)
#       - income service (list of objects)
#       - capital gain (list of objects)
#       - reimbursed expenditures
##############################################################################



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
