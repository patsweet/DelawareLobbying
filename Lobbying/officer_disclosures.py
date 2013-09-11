import csv
import json
from settings import officer_settings
from xml_parsers import parsePublicOfficerXML
from PublicOfficers import *


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


def instrumentOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year',
        'submitted_date', 'name', 'instrument', 'nature_of_ownership'
    ]
    with open(officer_settings["INSTRUMENTOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for inst in officer.instrument_ownership:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    inst.name,
                    inst.instrument,
                    inst.nature_of_ownership
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

def businessOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year', 'submitted_date',
        'name', 'name_of_ownership', 'position_of_management'
    ]
    with open(officer_settings["BUSINESSOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for item in officer.business_enterprise:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    item.name,
                    item.name_of_ownership,
                    item.position_of_management
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

def professionalOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year', 'submitted_date',
        'organization_name', 'address', 'type_of_practice', 'management_position'
    ]
    with open(officer_settings["PROOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for item in officer.pro_organization:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    item.organization_name,
                    item.address,
                    item.type_of_practice,
                    item.management_position
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

def incomeOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year', 'submitted_date',
        'income_source_type_id', 'income_source_type', 'income_source'
    ]
    with open(officer_settings["INCOMEOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for item in officer.income_service:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    item.income_source_type_id,
                    item.income_source_type,
                    item.income_source,
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

def capitalOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year', 'submitted_date',
        'capital_gain_name'
    ]
    with open(officer_settings["CAPITALGAINOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for item in officer.capital_gain:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    item.capital_gain_name
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

def reimbursedOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year', 'submitted_date',
        'expenditure_source'
    ]
    with open(officer_settings["REIMBURSEDOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for item in officer.reimbursed_expenditures:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    item.expenditure_source
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

def giftsOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year', 'submitted_date',
        'gift_type_id', 'gift_type', 'gift_source', 'gift_value'
    ]
    with open(officer_settings["GIFTSOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for item in officer.gifts:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    item.gift_type_id,
                    item.gift_type,
                    item.gift_source,
                    item.gift_value
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

def boardsOut(officers):
    header = [
        'last_name', 'first_name', 'position', 'year', 'submitted_date',
        'membership_type_id', 'membership_type', 'membership_name',
        'membership_address'
    ]
    with open(officer_settings["BOARDSOUT"], 'w+') as ofile:
        ofile.write("|".join(header) + "\n")
        for officer in officers:
            for item in officer.board_membership:
                out = [
                    officer.last_name,
                    officer.first_name,
                    officer.state_position,
                    officer.year,
                    officer.submitted_date,
                    item.membership_type_id,
                    item.membership_type,
                    item.membership_name,
                    item.membership_address
                ]
                out = [o if o else '' for o in out]
                ofile.write("|".join(out) + "\n")

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
            row = [
                item.strip().decode('cp1252', 'replace')
                    .encode('ascii', 'replace') for item in row
                ]
            xml_data = parsePublicOfficerXML(row[6])
            officer = PublicOfficer(
                first_name=row[0],
                middle_name=row[1],
                last_name=row[2],
                state_position=row[3],
                submitted_date=row[4],
                year=row[5],
                instrument_ownership=xml_data.get(
                    'instrument_ownership', None),
                business_enterprise=xml_data.get(
                    'business_enterprise', None),
                pro_organization=xml_data.get('pro_organization', None),
                constructive_control=xml_data.get(
                    'constructive_control', None),
                creditor=xml_data.get('creditor', None),
                income_service=xml_data.get('income_service', None),
                capital_gain=xml_data.get('capital_gain', None),
                reimbursed_expenditures=xml_data.get(
                    'reimbursed_expenditures', None),
                honoraria=xml_data.get('honoraria', None),
                gifts=xml_data.get('gifts', None),
                source_of_income=xml_data.get('source_of_income', None),
                board_membership=xml_data.get('board_membership', None),
                filename = row[7]
            )
            officers.append(officer)
        jsonfile.write(
            json.dumps(
                officers, cls=OfficerEncoder, sort_keys=True, indent=4,
                separators=(',', ': ')
            )
        )
        # Output to pipe-delimited files
        instrumentOut(officers)
        businessOut(officers)
        professionalOut(officers)
        incomeOut(officers)
        capitalOut(officers)
        reimbursedOut(officers)
        giftsOut(officers)
        boardsOut(officers)

if __name__ == '__main__':
    main()