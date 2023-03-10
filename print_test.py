from main import Employee, Developer, Manager
import datetime

### Initialize variables
developer_satoshi = Developer('Satoshi', 'Nakamoto', 100000, 'C++')
developer_vitalik = Developer('Vitalik', 'Buterin', 150000, 'Solidity')
manager_elon = Manager('Elon', 'Musk', 250000, [developer_satoshi, developer_vitalik])
manager_elon.add_emp(developer_satoshi)
manager_elon.add_emp(developer_vitalik)
manager_elon.remove_emp(developer_vitalik)
my_date = datetime.date(2023, 1, 16)

### Testing
print(f'Number of employees:', Employee.num_emp)
print(f'Salary of Satoshi before raise:', developer_satoshi.salary)
developer_satoshi.apply_raise()
print(f'Salary of Satoshi after raise:', developer_satoshi.salary)
print(f'Last name of Elon:', manager_elon.last_name)
print(f'Full name of Vitalik:', developer_vitalik.full_name)
print(f'Programming language of Satoshi:', developer_satoshi.pl)
print(f'Manager Elon supervises the following employees:', manager_elon.print_emp())
print(f'Check for isinstance:', isinstance(manager_elon, Manager))
print(f'Check for subclass:', issubclass(Developer, Employee))
print(f'Check if given date is workday:', Employee.is_workday(my_date))
print(f'Check repr:', repr(developer_satoshi))
print(f'Check str:', str(developer_satoshi))
print(f'Combined salaries:', developer_satoshi + developer_vitalik)