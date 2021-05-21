'''
Property is used for getter and setter functions

to run this code:
$ python3 property_decorators.py
'''

class Employee:
    def __init__(self, name):
        self.name = name
    
    '''
    As you can see this property decorator has change this email function into property
    which means you can use it as obj.email and don't need obj.email()
    '''
    @property
    def email(self):
        return f'{self.name}@gmail.com'


    '''
    This setter method gives you flexibility to change the email property that you have created
    '''
    @email.setter
    def email(self, email):
        self.name = email.split('@')[0]

    

ali_emp = Employee('alihaider')
print(f'Email is :{ali_emp.email}')

ali_emp.email = 'ahaider@gmail.com'
print(f'Email is changed :{ali_emp.email}') 