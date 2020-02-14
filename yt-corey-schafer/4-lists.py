# list
courses = ['History', 'Math', 'Physics']

print(courses[-1]) # can be negative

courses.append('Art')
courses.insert(1, 'Music')
print(courses)

courses_2 = ['Education', 'Painting']

# extend takes only one argument (a list) and mutates original list
courses.extend(courses_2)
print(courses)

last = courses.pop()

# Sorting:
numbers = [1, 3, 3, 2, 4, 8, 7, 6]
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)

# sorting without modifying original using global sorted function
numbers_1 = [1, 3, 3, 2, 4, 8, 7, 6]
sorted_numbers = sorted(numbers_1)
print(sorted_numbers)


print(min(numbers))
print(max(numbers))
print(sum(numbers))

# finding values
courses_1 = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('Math')) # -> index


print('Art' in courses_1) # -> false

# looping
for course in courses_1:
  print(course)

# if you want to loop with index, wrap list in enumerate()
# enumerate will return index and value
for index, course in enumerate(courses_1):
  print(index, course)

for index, course in enumerate(courses_1, start=2):
  print(index, course)

# using join and split
courses_str = ', '.join(courses_1)
print(courses_str)
courses_from_str = courses_str.split(', ')
print(courses_from_str)