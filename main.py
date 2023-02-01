
import datetime

class Employee:

    num_emp = 0
    raise_amount = 1.08
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
        self.email = first_name + "@company-name.com"

        Employee.num_emp +=1
    
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

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
    pass

### Initialize variables
employee_satoshi = Developer.from_str('Satoshi-Nakamoto-100000')
employee_vitalik = Developer.from_str('Vitalik-Buterin-150000')
employee_elon = Employee('Elon', 'Musk', 250000)
my_date = datetime.date(2023, 1, 16)

### Testing
print(f'Number of employees:', Employee.num_emp)
print(f'Salary of Satoshi:', employee_satoshi.salary)
print(f'Last name of Elon:', employee_elon.last_name)
print(f'Full name of Vitalik:', Employee.full_name(employee_vitalik))
print(f'Check if given date is workday:', Employee.is_workday(my_date))