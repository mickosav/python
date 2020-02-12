# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
list_1[0] = 'Art'
#list_1.append('Art')

print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

# tuple_1[0] = 'Art' # -> throws error
print(tuple_1)
print(tuple_2)

# tuples don't have as many methods as a list
# because a lot of list methods involve mutating values, and tuples are immutable
# other than that, they are pretty much the same as lists
# (we can loop through them, access values and so on)
