'''
@author: amayamunoz
'''
from builtins import False, True

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def sub_from_first(num1, num2):
    subNums = (num1 - num2)
    return(subNums) 

x = sub_from_first(12, 10)

print(x) 

#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def numCalc(num1, div, mult, add):
    totalCalc = num1 /div * mult + add
    return totalCalc

y = numCalc (2, 7, 43, 24)

print(y)

#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def check_num(num1, num2):
    equalNum = num1 == num2
    
    if(equalNum == num1 and num2):
        True 
    else:
        False
    return equalNum

z = check_num(6, 6)

print(z)

#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def compare_num(num1, num2):
    
    if(num1 > num2):
        return num1
    if(num1 < num2):
        return num2
    elif(num1 == num2)
        return num1
    
p = compare_num(6,7)

print(p)

#5) Define a function that takes in two words and returns a string that contains both words combined.
def joined_words(word1, word2):
    together = word1 + word2
    
    return together 
w = joined_words("good", "afternoon")

print(w)

#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def tri_num(num1, num2, num3):
    
    if(num1 == num2):
        return True
    elif(num1 == num3):
        return True
    else:
        return False
    return 

n = tri_num(4, 7, 4)

print(n)

#7) Define a function that prints your name.
def my_name(name):
    name = name[0:]
    return name

b = my_name("lezly")

print(b)
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def my_favorite_color(color):
    favColor = "red"
    
    if(favColor == color):
        print("That's my favorite color!")
    else:
        print("That is not my favorite color. Try again.")
    return 

t = my_favorite_color("red")
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def reach_zero(num1):
    
    while(num1 > 0):
        num1 = num1 - 1
        print(num1)
    return 

reach_zero(9)

'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.
def cap_first_name(name):
    name = name[0:].upper()
    return name 

q = cap_first_name("lezly")

print(q)


