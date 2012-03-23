import sys

__author__ = 'MK'

# global parameters
temp_val = 0
degree = ['Celsius', 'Farenheit']


#main program
temp_val = (sys.argv[1])
degree = (sys.argv[2])

# Celsius to Farenheit
if degree =='Celsius':
    temp_val=float(temp_val)
    far_value = temp_val * 9.0 / 5.0 + 32
    print("%.2f" %far_value)

# Farenheit to Celsius
else:
    temp_val=float(temp_val)
    celsius_value = (temp_val - 32 ) * 5 / 9
    print("%.2f" %celsius_value)

