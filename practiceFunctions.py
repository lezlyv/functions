'''
Created on Apr 25, 2020

@author: ITAUser
'''
from functools import total_ordering
from ctypes.test.test_pickling import name

def sum_two_numbers(num1, num2, num3):
    sumOfNums = num1 + num2 +num3
    return sumOfNums

x = sum_two_numbers(4, 5, 6)

print(x) 

x = sum_two_numbers(2, 2, 4)

print(x)



def taxCalc(subTotal, tax):
    taxAmount = subTotal * tax
    total = subTotal + taxAmount
    return total

y = taxCalc(152, .05)

print(y)



def taxCalc(subTotal, tax,):
    taxAmount = subTotal * tax
    total = subTotal + taxAmount
    
    if(total > 100):
        shipping = 0
    elif(total > 50):
        shipping = 10
    else:
        shipping - 5
       
    total = total + shipping 
    return total

y = taxCalc(152, .05)

print(y)

y = taxCalc(80, .05)

print(y)

y = taxCalc(10, .05)

print(y)



def capFirstName(name):
    name[0] = name[0].upper() + name[1:]
    return name

z = capFirstName ("lezly")
print(z) 






