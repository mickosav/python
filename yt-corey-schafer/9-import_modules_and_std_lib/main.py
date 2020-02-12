import my_module # this works because it's in the same directory
# when you import the module it runs all the code from the module
# if you run this, you will see print statement from my_module

# using import aliases
import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

# when using functions from module, they are not on global scope
index = my_module.find_index(courses, 'Math')
print(index)

index2 = mm.find_index(courses, 'Physics')
print(index2)

# importing only function and variable
from my_module import find_index, test as t

index3 = find_index(courses, 'History')
print(index3)
print(t)