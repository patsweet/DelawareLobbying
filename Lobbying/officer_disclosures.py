import csv
from settings import officer_settings
from .PublicOfficers import *


class OfficerEncoder(json.JSONEncoder):
    """
        Helper class to translate classes to
        JSON.
    """
    def default(self, obj):
        if not isinstance(obj, InstrumentOwnership) \
        and not isinstance(obj, BusinessEnterprise) \
        and not isinstance(obj, ProfessionalOrganization) \
        and not isinstance(obj, ConstructiveControl) \
        and not isinstance(obj, Creditor) \
        and not isinstance(obj, IncomeService) \
        and not isinstance(obj, CapitalGain) \
        and not isinstance(obj, ReimbursedExpenditure) \
        and not isinstance(obj, Honoraria) \
        and not isinstance(obj, Gift) \
        and not isinstance(obj, IncomeSource) \
        and not isinstance(obj, PublicOfficer) \
        and not isinstance(obj, BoardMembership):
            return super(MyEncoder, self).default(obj)
        return obj.__dict__

def main():
    """
    Parse csv, create master json file and pipe-delimited
    files for public officers.
    """
    officers = []
    with open(officer_settings['IFILE'], 'r') as csvfile, \
        open(officer_settings['JSONOUT'], 'w+') as jsonfile:
        record_id = 1
        reader = csv.reader(csvfile, delimiter='|')
        reader.next()  # Skip the header row.
        for row in reader:
            row = [item.decode]


if __name__ == '__main__':
    main()