"""Decorators: we can define as method and access as attribute"""


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@email.com"
      
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    

emp1 = Employee('satya', 'sravya')
emp2 = Employee('Corey', 'Schafer')

emp1.first = 'Guduri'
#still fetching initial first name
print(emp1.email)


class Employee1:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + "@email.com"

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ", 1)
        self.first = first
        self.last = last

emp1 = Employee('Satya', 'sravya')
emp1.fullname = "G Sravya"
print("fin")
print(emp1.__dict__)
print(emp1.email)
