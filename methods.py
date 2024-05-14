""" Regular Instance methods, class methods, static methods
"""
import datetime

class Employee:

    raise_amount = 1.04
    num_emplys = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@email.com"
        self.pay = pay
        # to check number of instances created from this class
        Employee.num_emplys += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    #class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    # class method alternative way of constructors
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    #wont take any class instance
    @staticmethod
    def is_workday(day):
        if day.weekday() == 7 or day.weekday() == 6 :
            return False
        return True


emp1 = Employee('satya', 'sravya', 5000)
emp2 = Employee('Corey', 'Schafer', 6000)

Employee.set_raise_amount(1.05)

print(emp1.raise_amount)
print(emp2.raise_amount)

emp3 = Employee.from_string('Guru-Teja-7000')
print(emp3.__dict__)


my_date = datetime.date(2024, 5, 10)
print(Employee.is_workday(my_date))
