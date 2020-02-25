class Employee:

    raise_ammount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_ammount
    
    # CLASSMETHODS:
    # classmethod is built in decorator
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_ammount = amount

    # class methods can be used as an alternative constructors
    # it means you can use them to create a multiple ways of creating our objects
    # eg. someone might want to create instance of an employee
    # but all they have is a sting, they want to pass it in and create employee from that

    # by convention alternate constructiors start with 'from'
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    # see real-world example of theese on datetime module

    # STATICMETHODS:
    # staticmethods don't pass in anything automatically
    # (class methods pass class, regular meth pass instanse)
    # they behave just like a regular function but we include them
    # because they have some kind of logical connection with the class

    # eg. function that takes in a date and return whether it was an workday
    # that would have an logical connection to the class, but it doesn't
    # depend on any instance or a class variable
    @staticmethod
    def is_workday(day):
        # just en example code:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # when to use classmethods:
    # if you don't access instance or a class anywhere in a function
    # you probably want to check if you can use a staticmethod in that place
     

emp_1 = Employee('Micko', 'Car', 3000)
emp_2 = Employee('Pera', 'Sisa', 4000)

Employee.set_raise_amt(1.06)
print(Employee.raise_ammount, emp_1.raise_ammount, emp_2.raise_ammount)
Employee.raise_ammount = 1.04
print(Employee.raise_ammount, emp_1.raise_ammount, emp_2.raise_ammount)
# you can also call class methods from an instances but that
# doesn't make a lot of sence, and I don't see people ever doing it
emp_1.set_raise_amt(1.5)
print(Employee.raise_ammount, emp_1.raise_ammount, emp_2.raise_ammount)


# alternate constructor:
emp_str_1 = 'John-Doe-6000'
new_emp_1 = Employee.from_string(emp_str_1)


# staticmethod
import datetime
my_date = datetime.date(2020, 2, 25)
print(Employee.is_workday(my_date))
