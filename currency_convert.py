import sys

########################################################################
# currency converter for EUR, USD and JPY with rates from March 23. 2012
# Michal Kalinic
# Python 3.2
# GPL 3.0
########################################################################

__author__ = 'MK'

#SAP: I did a few corrections, see #SAP

# global parameters
given_amount = 0
first_currency = ['EUR', 'USD', 'JPY']
second_currency = ['EUR', 'USD', 'JPY']
converted_value = 0

#main program
given_amount = (sys.argv[1])  # i tested only with arguments 200 EUR in USD, see output down
first_currency = (sys.argv[2])
second_currency = (sys.argv[3])

print( )#SAP

# EURO to other
def EUR_TO_OTHER ():
    global given_amount #SAP
    if first_currency =='EUR': #SAP
        # to USD
        second_currency == 'USD'
        given_amount=float(given_amount)
        converted_value = given_amount * 1.31981
        print(given_amount, first_currency, '=', "%.4f" %converted_value, 'USD') #SAP
        print('EUR foreign exchange reference rates as at 23. March 2012 \n') #SAP
        # to JPN
        second_currency == 'JPY'
        given_amount=float(given_amount)
        converted_value = given_amount * 109.55
        print(given_amount, first_currency, '=', "%.4f" %converted_value, 'JPY') #SAP
        print('EUR foreign exchange reference rates as at 23. March 2012')

# USD to other
def USD_TO_OTHER ():
    global given_amount
    if first_currency =='USD':
        # to EUR
        second_currency == 'EUR'
        given_amount=float(given_amount)
        converted_value = given_amount * (1/1.31981)
        print(given_amount, first_currency, '=', "%.4f" %converted_value, 'EUR \n' )
        print('USD foreign exchange reference rates as at 23. March 2012 \n')
        # to JPY
        second_currency == 'JPY'
        given_amount=float(given_amount)
        converted_value = given_amount * 83.00
        print(given_amount, first_currency, '=', "%.4f" %converted_value, 'JPY' )
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



EUR_TO_OTHER()
USD_TO_OTHER()
JPY_TO_OTHER()

'''
200.0 EUR = 263.9620 USD
EUR foreign exchange reference rates as at 23. March 2012

200.0 EUR = 21910.0000 JPY
EUR foreign exchange reference rates as at 23. March 2012
'''