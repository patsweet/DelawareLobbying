# Lobbying and Public Officer disclosures

This set of scripts translates the lobbyist and public officer disclosures into something useful, specifically a collection of pipe-delimited text files and two json files.

## Why so many files?

The scripts are broken up into five main components:

1. [PublicOfficers.py](https://bitbucket.org/thenewsjournal/lobbying-disclosures/src/16de73e19cfada3de550e5acc8a5e23e77965387/Lobbying/PublicOfficers.py?at=master)
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
2. [Lobbyists.py](https://bitbucket.org/thenewsjournal/lobbying-disclosures/src/16de73e19cfada3de550e5acc8a5e23e77965387/Lobbying/Lobbyists.py?at=master)
    - Models defining types of objects parsed from the XML string for lobbyists. It includes classes for:
        - Lobbyist
            - The main class that includes basic info on the lobbyist and lists of objects of the types below.
        - Employer
        - Expenditure
        - Gift
3. [officer_disclosures.py](https://bitbucket.org/thenewsjournal/lobbying-disclosures/src/16de73e19cfada3de550e5acc8a5e23e77965387/Lobbying/officer_disclosures.py?at=master)
    - Responsible for parsing the raw public officer data and outputting to the json and pipe-delimited files.
4. [lobby_disclosures.py](https://bitbucket.org/thenewsjournal/lobbying-disclosures/src/16de73e19cfada3de550e5acc8a5e23e77965387/Lobbying/lobby_disclosures.py?at=master)
    - Responsible for parsing the raw lobbying data and outputting to the json and pipe-delimited files.
5. [xml_parsers.py](https://bitbucket.org/thenewsjournal/lobbying-disclosures/src/16de73e19cfada3de550e5acc8a5e23e77965387/Lobbying/xml_parsers.py?at=master)
    - Contains two functions that take XML strings as input and return lists of objects for lobbying and public officer disclosures.
        1. parseLobbyistXML(xml_string)
            - Returns a list of expenditures and a list of gifts.
        2. parsePublicOfficerXML(xml_string)
            - Returns a dictionary of objects from PublicOfficers.py
