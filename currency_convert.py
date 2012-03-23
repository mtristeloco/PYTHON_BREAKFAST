import sys

__author__ = 'MK'

# global parameters
given_amount = 0
first_currency = ['EUR', 'USD', 'JPY']
second_currency = ['EUR', 'USD', 'JPY']
converted_value = 0

#main program
given_amount = (sys.argv[1])
first_currency = (sys.argv[2])
second_currency = (sys.argv[4])

# EURO to other
def EUR_TO_OTHER ():
    if first_currency =='EURO':
        # to USD
        second_currency == 'USD'
        given_amount=float(given_amount)
        converted_value = given_amount * 1.31981
        print("%.4f" %converted_value)
        print('EUR foreign exchange reference rates as at 23. March 2012')
    # to JPN
    if second_currency == 'JPY':
        given_amount=float(given_amount)
        converted_value = given_amount * 109.55
        print("%.4f" %converted_value)
        print('EUR foreign exchange reference rates as at 23. March 2012')

# USD to other
def USD_TO_OTHER ():
    if first_currency =='USD':
        # to USD
        if second_currency == 'EUR':
            given_amount=float(given_amount)
            converted_value = given_amount * (1/1.31981)
            print("%.4f" %converted_value)
            print('USD foreign exchange reference rates as at 23. March 2012')
        # to JPY
        if second_currency == 'JPY':
            given_amount=float(given_amount)
            converted_value = given_amount * 83.00
            print("%.4f" %converted_value)
            print('USD foreign exchange reference rates as at 23. March 2012')

# JPY to other
def JPY_TO_OTHER ():
    if first_currency =='JPY':
        # to USD
        if second_currency == 'USD':
            given_amount=float(given_amount)
            converted_value = given_amount * (1/83.0)
            print("%.4f" %converted_value)
            print('JPY foreign exchange reference rates as at 23. March 2012')
        # to EURO
        if second_currency == 'EUR':
            given_amount=float(given_amount)
            converted_value = given_amount * (1/109.55)
            print("%.4f" %converted_value)
            print('JPY foreign exchange reference rates as at 23. March 2012')

# i don't know how to print the result :-(
