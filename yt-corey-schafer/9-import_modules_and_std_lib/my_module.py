print('Hello from module')

test = 'Test String'

def find_index_micko(list, search_item):
    '''Find the index of a value in a sequence'''
    index = -1
    for i, value in enumerate(list): # ATTENTION: index is first item - I'm used to opposite in JS
        if value == search_item:
            index = i
            break

    return index

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1