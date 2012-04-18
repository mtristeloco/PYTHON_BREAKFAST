##############################################################
# Name:     num_converter.py
#
# Convert given number to and from decimal, hexadecimal and binary
#
# Michal Kalinic
# Python 3.2
# ##############################################################
import sys


__author__ = 'MK'
given_number = sys.argv[1]
number_type = given_number[0]
x = given_number[1:]


def binary_to_decimal_hexadecimal(x):
    if number_type == 'b':
        print ('BIN:', x)
        print ('DEC:', int(x, 2))
        print ('HEX:', hex(int(x, 2)))

def decimal_to_bin_hexadecimal(x):
    if number_type == 'd':
        print ('BIN:', bin(int(x)))
        print ('DEC:', x)
        print ('HEX:', hex(int(x)))

def hexadecimal_to_bin_decimal(x):
    if number_type == 'h':
        print ('BIN:', bin(int(x, 16)))
        print ('DEC:', int(x, 16))
        print ('HEX:', x)

binary_to_decimal_hexadecimal(x)
decimal_to_bin_hexadecimal(x)
hexadecimal_to_bin_decimal(x)