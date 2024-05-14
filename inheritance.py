"""
"""

""" Regular Instance methods, class methods, static methods
"""
import datetime

class Employee:
    
    raise_amount = 1.05 # class attr

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@email.com"
        self.pay = pay
 
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    #class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):

    raise_amount =  1.05

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, name):
        if name not in self.employees:
            self.employees.append(name)

    def remove_emp(self, name):
        if name in self.employees:
            self.employees.remove(name)

    def print_emps(self):
        for emp in self.employees:
            print("--- ", emp.fullname())




# Methos REsolution Order: first looks in Developer then crawls to employee
#to check this try print(help(dev1))

dev1 = Developer('satya', 'sravya', 5000, 'Python')
dev2 = Developer('Corey', 'Schafer', 6000, "java")

mgr = Manager('Neeraj', 'Kumar',8000, [dev1])

print(dev1.pay)
#picks up from child class not from parents
dev1.apply_raise()
print(dev1.pay)

# for new attr
print(dev1.lang)


print(mgr.email)
mgr.add_emp(dev2)
print(mgr.print_emps())
mgr.remove_emp(dev1)
print(mgr.print_emps())


#is instance or sub class

print(isinstance(mgr, Employee))
print(isinstance(mgr, Manager))
print(isinstance(mgr, Developer)) #bcz siblings


print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
