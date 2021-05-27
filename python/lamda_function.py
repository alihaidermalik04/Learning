'''
A lambda function can take any number of arguments, but can only have one expression.

to run this code:
$ python3 lamda_function.py
'''

def power(num):
    return lambda a : a**num

test = power(2)

test2 = test(5)

print(test2)
