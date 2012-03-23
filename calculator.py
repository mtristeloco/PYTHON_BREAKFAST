import sys

##############################################################
# commandline calculator with fce +-*/
# MK
# Python 3.2
##############################################################

__author__ = 'MK'

first_number = 0
math_funkt = 0
second_number = 0

#def numbers
first_number = (sys.argv[1])
math_funkt = (sys.argv[2])
second_number = (sys.argv[3])

# convert numbers to float numbers
def convertString(str):
    try:
        returnValue = int(str)
    except ValueError:
        returnValue = float(str)
    return returnValue

# math functions defined
def addition(first_number, second_number):
    return convertString(first_number) + convertString(second_number)

def subtraction(first_number, second_number):
    return convertString(first_number) - convertString(second_number)

def multiplication(first_number,second_number):
    return convertString(first_number) * convertString(second_number)

def division(first_number, second_number):
    return convertString(first_number) / convertString(second_number)

#main program
if math_funkt == "+":
    print (addition(first_number, second_number))
elif math_funkt == "-":
    print (subtraction(first_number, second_number))
elif math_funkt == "*":
    print(multiplication(first_number, second_number))
elif math_funkt == "/":
    print(division(first_number, second_number))