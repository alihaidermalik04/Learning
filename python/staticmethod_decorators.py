'''
Helps to create static methods inside a class
'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def check(age):
        if age>15:
            print('Go to collage')
        else:
            print('Go to school')

    
    
ali_obj = Student('Ali Haider', 90)
ali_obj.check(11)
