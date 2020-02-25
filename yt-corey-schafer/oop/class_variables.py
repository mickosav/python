# class variables are variables that are shared amongst all instances of a class
class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)
        Employee.num_of_emps += 1
        # ^ using class directly because we can't think of an usecase where
        # we want to let instance or class inheriting Employee to override num_of_emps
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # if you try to acces the variable from the instance it will first check
        # if instance contains that attribute, if it doesn't it will check on class
        # or any class that we enherit from
        self.pay = int(self.pay * self.raise_amount)
        # ^ we are using 'self.raise_amout' here because we want to let
        # instance or any class that inherits from Employee override
        # raise_amount attribute if needed


emp_1 = Employee('Micko', 'Savovic', 30000)
emp_2 = Employee('Pera', 'Peric', 40000)

# prints namespace of emp_1 instance
print(emp_1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05
print(emp_1.raise_amount)

print(Employee.num_of_emps)