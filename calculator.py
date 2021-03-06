import sys

##############################################################
# commandline calculator with fce +-*/
# Michal Kalinic
# Python 3.2
# GPL 3.0
##############################################################

__author__ = 'MK'

first_number = 0
math_funkt = 0
second_number = 0

#def numbers and fce
first_number = (sys.argv[1])    # SAP arguments need to be given:
                                # Edit Configurations->Script parameters, I tested with
                                # 18 + 3, but you need to do some changes to the others in order to work
math_funkt = (sys.argv[2])      # result 21
second_number = (sys.argv[3])

# math functions defined
def addition(first_number, second_number):
    return int(first_number) + int(second_number)

def subtraction(first_number, second_number):
    return int(first_number) - int(second_number)

def multiplication(first_number,second_number):
    return int(first_number) * int(second_number)

def division(first_number, second_number):
    return int(first_number) / int(second_number)

#main program
if math_funkt == "+":
    print (addition(first_number, second_number))
if math_funkt == "-":
    print (subtraction(first_number, second_number))
if math_funkt == "*":
    print(multiplication(first_number, second_number))
if math_funkt == "/":
    print(division(first_number, second_number))
