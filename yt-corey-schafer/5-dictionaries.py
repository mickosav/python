# https://realpython.com/python-dicts/
# In other laguages called hashmaps or associative arrays

# Key must be of a type that is immutable
# Key can appear in a dictionary only once
# Almost any type of value can be used as a dictionary key (integer, float, Boolean etc)
# A tuple can also be a dictionary key, because tuples are immutable


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 1: 'Hello'}

# accessing values
print(student['name'])
print(student[1])
# ^ if key doesn't exist this will throw exception

print(student.get('sadfasdf')) # -> None
print(student.get('323radsf', 'Not found')) # -> Not found

student['phone'] = '555-292019'
student['name'] = 'Micko'

print(student)

student.update({ 'name': 'Pera', (1, 2): 'test' })
print(student[(1, 2)])
print(student)

del student[(1, 2)]
phone = student.pop('phone')
print(student)
print(len(student))

print(student.keys()) # just keys
print(student.values()) # just values
print(student.items()) # list of key-value pairs
# Looping
for key, value in student.items():
  print(key, value)