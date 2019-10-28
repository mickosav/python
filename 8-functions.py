# def is shor for 'definition'

def first_function():
    pass # indicates that nothing happens—the function, class or loop is empty

print(first_function)
print(first_function()) # -> None

def hello_func():
    print('Hello function!')

hello_func()
hello_func()
# DRY - dont repeat yourself

def return_hello():
    return 'Hello function.'

print(return_hello().upper())

def greet (name, greeting = 'Hello'): # required params have to come before default ones
    return f'{greeting}, {name}!'

print(greet('Micko', 'Ola'))
print(greet('Micko'))

def student_info(*args, **kwargs): # allows us to accept arbitrary number of positional or keyword arguments (like rest operator in JS)
    print(args) # -> ('Math', 'Art') - Tuple with positional args
    print(kwargs) # -> {'name': 'John', 'age': 22} - Dict of keyword args

student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = { 'name': 'John', 'age': 22 }
student_info(*courses, **info) # now works like destructure operator in JS

courses_tuple = ('CompSci', 'Physics')
student_info(*courses_tuple, **info)
student_info(*info, **info)


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    # ^ this is called doc string, starts with 3 "" and is used to explain what function does

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(1991, 12))