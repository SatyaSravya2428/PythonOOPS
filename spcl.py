"""Special / Magic methods"""

#dunder - double underscores 

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

    #unambiguous representation for debugging purpose
    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self) -> str:
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


emp1 = Employee('satya', 'sravya', 5000)
emp2 = Employee('Corey', 'Schafer', 6000)

print(emp1)

# adding two employee salaries
print(emp1 + emp2)

print(len(emp1))
