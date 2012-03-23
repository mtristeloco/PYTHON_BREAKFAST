##############################################################
# Program revers String
# Python 3.2
##############################################################
import sys

__author__ = 'MK'

# global
s = ''

# define revers function
def rev(s): return s[::-1]

# entry point
s = (sys.argv[1])
s = rev(s)
print(s)


