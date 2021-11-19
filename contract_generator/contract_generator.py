"""
Generates contracts for employees according to the database of employees and contract templates.
Database and templates are in separate .txt files.
Generated contracts are separate .txt files.
"""

TEMPLATE_PATH = r'X:\IT\PYTHON\EXERCISES\contract_generator'
OUTPUT_PATH = r'X:\IT\PYTHON\EXERCISES\contract_generator'
EMPLOYEE_DB_PATH = r'X:\IT\PYTHON\EXERCISES\contract_generator\employees.txt'

TEMPLATES = ['salary change', 'job change', 'contract prolongation']


def main():
    generate_contract(emp_code(), contract_type())


def emp_code():
    with open(EMPLOYEE_DB_PATH, 'r') as file:
        employees = eval(file.read())

        while True:
            ecode = input('Please enter an employee code: ')
            if ecode in employees.keys():
                return ecode
            else:
                print('Code not found.')


def contract_type():
    print('Types of contracts available:')
    for temp in enumerate(TEMPLATES):
        print('{}) {}'.format(*temp))

    while True:
        try:
            n = int(input('Please choose a number of contract to generate: '))
        except ValueError:
            print('Invalid, input not a number.')
            continue
        if n in list(range(0, len(TEMPLATES))):
            return n


def load_employees_db(path):
    with open(path, 'r') as file:
        return eval(file.read())


def load_template(ctype):
    template_filename = '{}\\{}.txt'.format(TEMPLATE_PATH, TEMPLATES[ctype].replace(' ', '_'))
    with open(template_filename, 'r') as file:
        return file.read()


def generate_contract(empcode, ctype):
    output_filename = '{}\\{}_{}.txt'.format(OUTPUT_PATH, empcode, TEMPLATES[ctype].replace(' ', '_'))
    with open(output_filename, 'w') as file:
        employees_data = load_employees_db(EMPLOYEE_DB_PATH)
        output_text = load_template(ctype).format(**employees_data[empcode])
        file.write(output_text)
        print('Contract file {} has been generated.'.format(output_filename))


main()
