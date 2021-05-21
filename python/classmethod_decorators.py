'''
classmethod decorators helps us to make class methods.

to run this code:
$ python3 classmethod_decorators.py
'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @classmethod
    def get_per(cls, name, marks):
        print(f'{name} got {(marks/200)*100} percentage')

    
    
ali_obj = Student('Ali Haider', 90)
ali_obj.get_per('Ali Haider', 90)