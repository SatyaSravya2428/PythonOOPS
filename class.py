""" Class Vs Methods, Attributes
"""

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


emp1 = Employee('satya', 'sravya', 5000)
emp2 = Employee('Corey', 'Schafer', 6000)


print(emp1.__dict__)
print(emp1.first)
print(emp1.fullname())
# self is imp as this will be passed this way in the backend
print(Employee.fullname(emp1)) 

print(emp1.raise_amount)
print(emp2.raise_amount)

#now that emp1 instance got its own replace_amount variable it woudnt go to main instance for reference
emp1.raise_amount = 1.05

print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.raise_amount(1.05)

print(emp1.raise_amount)
print(emp2.raise_amount)