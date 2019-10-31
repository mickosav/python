nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# using comprehension
my_list = [n for n in nums]
print(my_list)

# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

# using map
my_list = map(lambda n: n*n, nums)
print(list(my_list)) # without convering it to list it printed '<map object at 0x10ea00eb8>'

my_list = [n * n for n in nums]
print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# using filter
my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list))

my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# I want a (leter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for l in 'abcd':
    for n in range(0, 4):
        my_list.append((l, n))
print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names,heros)))

# I want a dict {'name': 'hero'} for each name, hero in zip(names,heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# If name is not equal to Peter
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

# Set Comprehensions
nums = [1,1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# use {} like with dict, but we don't have : (colon)
my_set = {n for n in nums}
print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)