import random
import math
import datetime
import calendar
import os
# ^ modules from the standard library

courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today) # -> YYYY-MM-DD
print(calendar.isleap(2004))

print(os.getcwd()) # -> current working directory

# if you want to find the module location print it's __file__ property - it reads as dunder file
# Dunder - (Double UNDERscore)
print(os.__file__)