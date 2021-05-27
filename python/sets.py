'''
sets in python are similar to sets in maths.
These sets are also represented by {} and have uninot and intersection methods.

to run this code:
$ python3 sets.py
'''

set1 = {'apple', 'mango', 'banana'}
set2 = {'watermelon', 'cherry', 'mango'}

print(f'UNION ----- set1 U set2: {set1.union(set2)}')
print(f'INTERSECTION ---- set1 || set2: {set1.intersection(set2)}')

'''
Another cool thing
'''

my_fav = {'mango', 'apple', 'gawa'}

if {'apple', 'mango'} <= my_fav:
    print('Yes..!!! they are my fav fruits')