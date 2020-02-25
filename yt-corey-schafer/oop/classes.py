class Employee:
    # recieves instance as first argument
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Micko', 'Savovic', 30000)
emp_2 = Employee('Pera', 'Peric', 49030)

print(emp_1.fullname())
# you can also call method on the class directly and pass in instance
# that will be passed in as 'self' argument
print(Employee.fullname(emp_1))
# ^ this is what's happening in the backgound when you execute emp_1.fullname()
