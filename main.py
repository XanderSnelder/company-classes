
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
