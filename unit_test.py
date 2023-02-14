from main import Employee, Developer, Manager
import unittest
import datetime

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp_1 = Employee("Satoshi", "Nakamoto", 50000)
        self.emp_2 = Employee("Vitalik", "Buterin", 60000)
    
    def test_email(self):
        self.assertEqual(self.emp_1.email, "Satoshi.Nakamoto@company.com")
        self.assertEqual(self.emp_2.email, "Vitalik.Buterin@company.com")
        
    def test_full_name(self):
        self.assertEqual(self.emp_1.full_name, "Satoshi Nakamoto")
        self.assertEqual(self.emp_2.full_name, "Vitalik Buterin")
        
    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.salary, 54000)

        self.emp_2.apply_raise()
        self.assertEqual(self.emp_2.salary, 64800)
        
    def test_set_raise_amt(self):
        Employee.set_raise_amt(1.1)
        self.assertEqual(Employee.raise_amount, 1.1)
        self.assertEqual(self.emp_1.raise_amount, 1.1)
        
    def test_from_str(self):
        emp_str = "Vitalik-Buterin-60000"
        emp = Employee.from_str(emp_str)
        self.assertEqual(emp.first_name, "Vitalik")
        self.assertEqual(emp.last_name, "Buterin")
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
        self.dev_1 = Developer("Satoshi", "Nakamoto", 70000, "C++")
        self.dev_2 = Developer("Vitalik", "Buterin", 80000, "Solidity")
    
    def test_str(self):
        self.assertEqual(str(self.dev_1), "Developer: Satoshi Nakamoto with salary 70000 and programming language C++")
        self.assertEqual(str(self.dev_2), "Developer: Vitalik Buterin with salary 80000 and programming language Solidity")
        
    def test_repr(self):
        self.assertEqual(repr(self.dev_1), "Developer('Satoshi', 'Nakamoto', '70000', 'C++')")
        self.assertEqual(repr(self.dev_2), "Developer('Vitalik', 'Buterin', '80000', 'Solidity')")
        
    def test_add(self):
        dev_3 = Developer("Sergey", "Nazarov", 60000, "Solidity")
        self.assertEqual(self.dev_1 + dev_3, 130000)
        
class TestManager(unittest.TestCase):
    
    def setUp(self):
        self.emp_1 = Employee("Satoshi", "Nakamoto", 50000)
        self.emp_2 = Employee("Vitalik", "Buterin", 60000)
        self.mgr_1 = Manager("Elon", "Musk", 90000, [self.emp_1])
    
    def test_add_emp(self):
        self.mgr_1.add_emp(self.emp_2)
        self.assertEqual(len(self.mgr_1.employees), 2)
        self.assertIn(self.emp_2, self.mgr_1.employees)
        
    def test_remove_emp(self):
        self.mgr_1.remove_emp(self.emp_1)
        self.assertEqual(len(self.mgr_1.employees), 0)
        self.assertNotIn(self.emp_1, self.mgr_1.employees)
        
    def test_print_emp(self):
        self.assertEqual(self.mgr_1.print_emp(), "Satoshi Nakamoto\n")
        
    def test_str(self):
        self.assertEqual(str(self.mgr_1), "Manager: Elon Musk with salary 90000")
        
    # def test_repr(self):
    #     self.assertEqual(repr(self.mgr_1), "Manager('Elon', 'Musk', '90000', employees=[<employee.Employee object at {}>])".format(hex(id(self.emp1))))
        
    def test_add(self):
        mgr_2 = Manager("Bill", "Gates", 80000)
        self.assertEqual(self.mgr_1 + mgr_2, 170000)

if __name__ == '__main__':
    unittest.main()
