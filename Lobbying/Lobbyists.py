# Models for the lobbyist disclosures.
#     __          __    __          _      __
#    / /   ____  / /_  / /_  __  __(_)____/ /______
#   / /   / __ \/ __ \/ __ \/ / / / / ___/ __/ ___/
#  / /___/ /_/ / /_/ / /_/ / /_/ / (__  ) /_(__  )
# /_____/\____/_.___/_.___/\__, /_/____/\__/____/
#                         /____/
##############################################################################
class Employer(object):
    """
    Employer info
    """
    def __init__(self, employer_id, legal_name, address_1, address_2, city,
        state, zip_code):
        self.employer_id = employer_id
        self.legal_name = legal_name
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        return "%s (%s)" % (self.legal_name, self.employer_id)


class Gift(object):
    """A single gift from a lobbyist"""
    def __init__(self, item_id, disclosure_id, employer, gift_date, poid,
        poname, gift_description, gift_value):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.employer = employer
        self.gift_date = gift_date
        self.poid = poid
        self.poname = poname
        self.gift_description = gift_description
        self.gift_value = gift_value


class Expenditure(object):
    """
    A single disclosure by a lobbyist, including the employer information
    and the ammounts expended.
    """
    def __init__(self, item_id, disclosure_id, employer, employer_id,
        food_refreshments, entertainment, lodging_expenses, travel_expenses,
        recreation_expenses, gift_contributions):
        self.item_id = item_id
        self.disclosure_id = disclosure_id
        self.employer = employer
        self.employer_id = employer_id
        self.food_refreshments = food_refreshments
        self.entertainment = entertainment
        self.lodging_expenses = lodging_expenses
        self.travel_expenses = travel_expenses
        self.recreation_expenses = recreation_expenses
        self.gift_contributions = gift_contributions

    def get_total(self):
        return (self.food_refreshments + self.entertainment +
            self.lodging_expenses + self.travel_expenses +
            self.recreation_expenses + self.gift_contributions)

    def __str__(self):
        return "{}: ${:,.2f}".format(self.employer, self.get_total())


class Lobbyist(object):
    """
        Holds information on a single lobbyist
        including his employer info.
    """
    def __init__(self, record_id, first_name, last_name, occupation,
        lobbyist_only, employment_explanation, submitted_date, year, quarter,
        expenditures, gifts):
        self.record_id = record_id
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.lobbyist_only = int(lobbyist_only)
        self.employment_explanation = employment_explanation
        self.submitted_date = submitted_date
        self.year = year
        self.quarter = quarter
        self.expenditures = expenditures
        self.gifts = gifts

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()
