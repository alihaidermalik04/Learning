'''
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

to run this code:
$ python3 filter_function.py
'''

nums = [1,2,3,4,5,6,7]

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_nums = filter(is_even, nums)

for num in even_nums:
    print(num)