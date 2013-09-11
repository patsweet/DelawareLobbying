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
        os.path.join("data_out", "public_officers.txt"))
}