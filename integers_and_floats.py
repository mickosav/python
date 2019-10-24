# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

print(3 / 2) # in python 2 this will be 1
print(3 // 2) # drops decimal points
num = 1
num += 1
num *= 10

print(f'Num: {num}')
print(abs(-3))
print(round(3.75, 1))

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
# comparisons return Boolean values

# converting from string to integer:
# in python converting is called 'casting'

num_1 = '100'
num_2 = '200'
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)