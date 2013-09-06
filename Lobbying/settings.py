# CONSTANTS for the disclosures script.
# Place the filenames here.
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IFILE = os.path.join(BASE_DIR, "cleaned_data\Lobbyist database 2013.csv")
JSONOUT = os.path.join(BASE_DIR, "data_out\lobbyists.json")
GIFTSOUT = os.path.join(BASE_DIR, "data_out\lobbyist_gifts.txt")
EXPENDOUT = os.path.join(BASE_DIR, "data_out\lobbyist_expenditures.txt")
