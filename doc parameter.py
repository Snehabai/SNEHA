# File: example.py

def add(a, b):
    '''
    This function adds two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The sum of the two numbers.
    '''
    return a + b

print(add.__doc__)  # This will print the docstring of the add function
'''
Purpose:
The purpose of the __doc__ attribute is to provide a way to access
the documentation string of an object programmatically.
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
It is used to document what the object does, its parameters, its return values, and any other relevant 
'''
