python_list = [True, True, True]

print(all(python_list))

'''
how all works under the hood:
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
'''

#practical use case of all
scores = [32, 45, 12, 67, 48, 92, 41]

#inline for
#syntax [expression for item in iterable]
squares = [list_element**2 for list_element in python_list]
print(squares)
