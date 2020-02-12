'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'global x'

def func_1():
    print(x) # -> prints global x

func_1()

def func_2():
    x = 5 # creates new x locally, doesn't change global one
    print(x)

func_2()
print(x)

def func_3():
    global x # this says we want to work with global x variable
    x = 'lala x'
    print(x)

func_3()
print(x)

def func_4(param):
    param = 4 # you can override params
    print(param)

func_4('micko')

m = min([5, 1, 4, 5, 9, 7]) # python is builtin function
print(m)

# if you want to see all builtin function you can
import builtins
print(dir(builtins)) # dir gets an list of an attributes of given object

# you can accidentaly override builtin function
def min(): pass
# m = min([5, 2, 1, 6]) # this will throw error
print(m)

def layer_1():
    x = 'Jebeni x'
    def layer_2():
        print(x)
        def layer_3():
            print(x)
            def layer_4():
                print(x)
            layer_4()
        layer_3()
    layer_2()
layer_1()


# closure example
def make_counter():
    i = 1
    def increase():
        nonlocal i # this will search in enclosing scopes, but it wont bubble up to global scope
        i += 1
    return increase

count = make_counter()

count()
count()
count()

# def func_5():
#     nonlocal x # throws an error - it wonnt look in global scope
#     x = 1

