# youtube.com/watch?v=FsAPt_9Bf3U
# closure
def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function

hi_func = outer_function('yoo')
bye_func = outer_function('bye')
hi_func()
bye_func()

# decorator is a function that takes in another function as an argument
# adds some kind of functionality and returns a new function
# without altering the source code if the function passed in
def decorator_funtion(original_function):
    def wrapper_function():
        print('wrapper executed this before "{}"'.format(original_function.__name__))
        return original_function()

    return wrapper_function

def display():
    print('display function ran')
display = decorator_funtion(display)
 # ^ this is the same as using #decorator_funtion before function definition
 # but it wouldn't work if 'display' function had any arguments
@decorator_funtion
def display_decorated():
    print('decorated display ran')

display()
display_decorated()

# example of proper decorator
def decorator(original_function):
    def wrapper_function(*args, **kwargs): # if you don't pass all arguments to the function you are decorating TypeError will be thrown
        print('wrapper executed this before "{}"'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function

@decorator
def display_info(name, age):
    print('display_info ran with arguments "{}" and "{}"'.format(name, age))

display_info('Micko', 838)

# decorators with class
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, *kwargs)

@decorator_class
def display_info_class_decorated(name, age):
    print('display_info ran with arguments "{}" and "{}"'.format(name, age))

display_info_class_decorated('Pera', 33)

# NOTE: function decorators are used more often so we will continue with them

def my_logger(orig_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))

    return wrapper