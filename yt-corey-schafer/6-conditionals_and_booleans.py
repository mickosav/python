# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
# Object Indentity: is
# ^ checking if the values have the same id (if they are pointing to the same object in memory)

# comparisons return Boolean values

language = 'javascripttt'

if language == 'python':
    print('It\'s python!')
elif language == 'javascript':
    print('It\'s JS!')
else:
    print('Don\'t know it.. :(')
# Pyton doesn't have switch statements - if/elif looked clean enough so they didn't put it in

# Logical operators (and, or, not):

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in == True:
    print('Your request to delete user is approved!')
else:
    print('Get out!')

if not logged_in:
    print('Please log in.')
else:
    print('Wellcome!')

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(id(a))
print(id(b))
print(a == b) # if values are equal
print(a is b) # if ids are equal
print(id(a) == id(b)) # ^ same as this
print(a is c)

# False values (when used in condition):
# False
# None
# Zero of any numeric value
# Any empty sequence: '', (), []
# Any empty mapping: {}

# True values:
# Everything else

condition = ['']

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')