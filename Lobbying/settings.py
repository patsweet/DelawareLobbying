# CONSTANTS for the disclosures script.
# Place the filenames here.
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

lobby_settings = {
    "IFILE": os.path.join(BASE_DIR,
        os.path.join("cleaned_data", "Lobbyist database 2012.csv")),
    "JSONOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "lobbyists.json")),
    "GIFTSOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "lobbyist_gifts2012.txt")),
    "EXPENDOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "lobbyist_expenditures2012.txt"))
}

officer_settings = {
    "IFILE": os.path.join(BASE_DIR,
        os.path.join("cleaned_data", "Public Officer 2012.csv")),
    "JSONOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "public_officers.json")),
    "PUBOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "public_officers.txt")),
    "INSTRUMENTOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "instrument_ownership.txt")),
    "BUSINESSOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "business_enterprise.txt")),
    "PROOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "professional_organization.txt")),
    "INCOMEOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "income_services.txt")),
    "CAPITALGAINOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "capital_gains.txt")),
    "REIMBURSEDOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "reimbursed_expenditures.txt")),
    "GIFTSOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "officer_gifts.txt")),
    "BOARDSOUT": os.path.join(BASE_DIR,
        os.path.join("data_out", "board_memberships.txt"))
}