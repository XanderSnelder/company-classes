from main import Employee, Developer, Manager
import unittest
import datetime

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp = Employee("John", "Doe", 50000)
    
    def test_email(self):
        self.assertEqual(self.emp.email.lower(), "john.doe@company.com")
        
        self.emp.first_name = "Jane"
        self.assertEqual(self.emp.email.lower(), "jane.doe@company.com")
        
    def test_full_name(self):
        self.assertEqual(self.emp.full_name, "John Doe")
        
        self.emp.first_name = "Jane"
        self.emp.last_name = "Smith"
        self.assertEqual(self.emp.full_name, "Jane Smith")
        
    def test_apply_raise(self):
        self.emp.apply_raise()
        self.assertEqual(self.emp.salary, 54000)
        
    def test_set_raise_amt(self):
        Employee.set_raise_amt(1.1)
        self.assertEqual(Employee.raise_amount, 1.1)
        self.assertEqual(self.emp.raise_amount, 1.1)
        
    def test_from_str(self):
        emp_str = "Jane-Smith-60000"
        emp = Employee.from_str(emp_str)
        self.assertEqual(emp.first_name, "Jane")
        self.assertEqual(emp.last_name, "Smith")
        self.assertEqual(emp.salary, 60000)
        
    def test_is_workday(self):
        # Monday
        day = datetime.date(2023, 2, 13)
        self.assertTrue(Employee.is_workday(day))
        
        # Saturday
        day = datetime.date(2023, 2, 18)
        self.assertFalse(Employee.is_workday(day))
        
class TestDeveloper(unittest.TestCase):
    
    def setUp(self):
        self.dev = Developer("John", "Doe", 50000, "Python")
    
    def test_str(self):
        self.assertEqual(str(self.dev), "Developer: John Doe with salary 50000 and programming language Python")
        
    def test_repr(self):
        self.assertEqual(repr(self.dev), "Developer('John', 'Doe', '50000', 'Python')")
        
    def test_add(self):
        dev2 = Developer("Jane", "Smith", 60000, "Java")
        self.assertEqual(self.dev + dev2, 110000)
        
class TestManager(unittest.TestCase):
    
    def setUp(self):
        self.emp1 = Employee("John", "Doe", 50000)
        self.emp2 = Employee("Jane", "Smith", 60000)
        self.mgr = Manager("Sue", "Murphy", 90000, [self.emp1])
    
    def test_add_emp(self):
        self.mgr.add_emp(self.emp2)
        self.assertEqual(len(self.mgr.employees), 2)
        self.assertIn(self.emp2, self.mgr.employees)
        
    def test_remove_emp(self):
        self.mgr.remove_emp(self.emp1)
        self.assertEqual(len(self.mgr.employees), 0)
        self.assertNotIn(self.emp1, self.mgr.employees)
        
    def test_print_emp(self):
        self.assertEqual(self.mgr.print_emp(), "John Doe\n")
        
    def test_str(self):
        self.assertEqual(str(self.mgr), "Manager: Sue Murphy with salary 90000")
        
    # def test_repr(self):
    #     self.assertEqual(repr(self.mgr), "Manager('Sue', 'Murphy', '90000', employees=[<employee.Employee object at {}>])".format(hex(id(self.emp1))))
        
    def test_add(self):
        mgr2 = Manager("Jim", "Johnson", 80000)
        self.assertEqual(self.mgr + mgr2, 170000)

if __name__ == '__main__':
    unittest.main()
