'''
Basically it passed function as an argument in beautiful way.

to run this code:
$ python3 decorators.py
'''

'''
Consider this dec function that takes a function as an argument.
'''

# def dec(func):
#     print('I will call a function')
#     return func

# def f(name):
#     print(f'hello {name}')

# test = dec(f)

# test('ali')


'''
Now lets see what decorator does 
* it allows to add functionality before and after a function
'''

# def dec(func):
#     def dec_inner(*args, **kwargs):

#         print(f'Greetings _________ {args[0]}')
#         f = func(*args, **kwargs)
#         print(f'Good Bye _________ {args[0]}')
#         return f
#     return dec_inner

# @dec
# def f(name):
#     print(f'how are you doing {name}')

# f('ali')

'''
Lets see another example
'''

# def check_non_zero(func):
#     def inner(*args):
#         denominator = args[1]
#         if denominator == 0:
#             print('Dnominator cant be zero')
#         else:
#             return func(*args)
#     return inner

# @check_non_zero
# def divide(numenator, denominator):
#     print(f'This is your result: {numenator/denominator}')

# test = divide(1,1)
