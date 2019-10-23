message = 'Hello Micko'
message_multiline = '''bla bla blalalll
hello lsakdjfl '''

print(message)
print(message_multiline)
print(len(message)) # length
print(type(message)) # -> <class 'str'>
print(message[0])

# slicing:
print(message[0:5]) # from (including) - to (excluding)
print(message[:5]) # from start
print(message[6:]) # from 6 to the end

# string methods
print(message.lower())
print(message.upper())
print(message.count('Micko'))
print(message.find('Hello'))
print(message.find('asdfasdfasdf')) # -> -1

message_pera = message.replace('Micko', 'Pera') # replace doesn't mutate state - it returnes new string
print(message_pera)

# concatenation
gretting = 'Hello'
name = 'Mickon'

print(gretting + ', ' + name + '. Welcome!')
print('{}, {}. Welcome!'.format(gretting, name))
# f-strings (available from v3.6)
print(f'{gretting}, {name.upper()}. Welcome!')
