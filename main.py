
import datetime

class Employee:

    num_emp = 0
    raise_amount = 1.08
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
        Employee.num_emp +=1
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last
    
    @full_name.deleter
    def full_name(self):
        print('Delete name!')
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_str(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, int(salary))
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):

    raise_amount = 1.12

    def __init__(self, first_name, last_name, salary, pl):
        super().__init__(first_name, last_name, salary)
        self.pl = pl

    def __repr__(self):
        return "Developer('{}', '{}', '{}', '{}')".format(self.first_name, self.last_name, self.salary, self.pl)

    def __str__(self):
        return "Developer: {} {} with salary {} and programming language {}".format(self.first_name, self.last_name, self.salary, self.pl)

    def __add__(self, other):
        return self.salary + other.salary 

class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp) 

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        result = ''
        for emp in self.employees:
            result += f"{emp.full_name}\n"
        return result
    
    def __repr__(self):
        return "Manager('{}', '{}', '{}', employees={})".format(self.first_name, self.last_name, self.salary, self.employees)
    
    def __str__(self):
        return "Manager: {} {} with salary {}".format(self.first_name, self.last_name, self.salary)
    
    def __add__(self, other):
        return self.salary + other.salary

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
print(f'Combined salaries:', developer_satoshi + developer_satoshi)
