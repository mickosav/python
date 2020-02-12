nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

print('\n')

for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

print('\n')

for num in nums:
    for letter in 'asdf':
        if letter == 'd':
            break
        print(num, letter)
    print(num)

print('\n')

# running loop certain number of times:

for i in range(10):
    print(i)

print('\n')

# first arg is starting value, second is last (not including)
for i in range(1, 11):
    print(i)

print('\n')

x = 10
while x <= 20:
    if x == 16:
        break
    print(x)
    x += 1