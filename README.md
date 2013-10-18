# Lobbying and Public Officer disclosures

This set of scripts translates the lobbyist and public officer disclosures into something useful, specifically a collection of pipe-delimited text files and two json files.

## Why so many files?

I wanted to try something different, and because there was so much variation in the data, I decided to write classes to hold the structure of various objects.
If I wanted a bare-bones, "let's get this s*** done" script, I could probably strip away alot of the extraneous stuff. I wanted practice putting it all together, though.

The scripts are broken up into six main components:

1. PublicOfficers.py
    - Models defining the types of objects we are parsing from the XML string for public officers. It includes classes for:
        - PublicOfficer
            - Main class that stores info on the public officer and lists of objects of the types below.
        - InstrumentOwnership
        - BusinessEnterprise
        - ProfessionalOrganization
        - ConstructiveControl
        - Creditor
        - IncomeService
        - CapitalGain
        - ReimbursedExpenditure
        - Honoraria
        - Gift
        - IncomeSource (not used)
        - BoardMembership
2. Lobbyists.py
    - Models defining types of objects parsed from the XML string for lobbyists. It includes classes for:
        - Lobbyist
            - The main class that includes basic info on the lobbyist and lists of objects of the types below.
        - Employer
        - Expenditure
        - Gift
3. officer_disclosures.py
    - Responsible for parsing the raw public officer data and outputting to the json and pipe-delimited files.
4. lobby_disclosures.py
    - Responsible for parsing the raw lobbying data and outputting to the json and pipe-delimited files.
5. xml_parses.py
    - Contains two functions that take XML strings as input and return lists of objects for lobbying and public officer disclosures.
        1. parseLobbyistXML(xml_string)
            - Returns a list of expenditures and a list of gifts.
        2. parsePublicOfficerXML(xml_string)
            - Returns a dictionary of objects from PublicOfficers.py
6. settings.py
    - Central location for all of the file paths for output and input.