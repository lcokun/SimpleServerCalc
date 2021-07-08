from pywebio.output import *
from pywebio.input import * 

put_markdown('## Simple Calculator')

def calculation():
    operation = radio('Choose an operation', options = ['Addition', 'Subtract', 'Multiply', 'Divide'] )
    
    if operation == 'Addition':
        x = input('Enter the first number', type = FLOAT)
        y = input('Enter the second number', type = FLOAT)
        z = x + y
    elif operation == 'Subtract':
        x = input('Enter the first number', type = FLOAT)
        y = input('Enter the second number', type = FLOAT)
        z = x - y
    elif operation == 'Multiply':
        x = input('Enter the first number', type = FLOAT)
        y = input('Enter the second number', type = FLOAT)
        z = x*y
    else:
        operation == 'Divide'
        x = input('Enter the first number', type = FLOAT)
        y = input('Enter the second number', type = FLOAT)
        z = x/y
    
    put_text('The output is:', z)
    
if __name__ == '__main__':
    calculation()
        