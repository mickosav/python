cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses) 
# sets don't care about ourder - if you execute print couple of times
# you will see order change

# sets cannot contain duplicates
cs_courses_1 = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses_1)

# they are also used to test whether a value is a part of a set
# this is called "membership test"
# sets do this a lot more efficiently that lists or tuples
print('Math' in cs_courses_1)

# they are also used to determine what values are shared
# or not shared with other sets
art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses)) # combining

# creating empty sets
empty_set = {} # this isn't set! It's a dict
empty_set = set()