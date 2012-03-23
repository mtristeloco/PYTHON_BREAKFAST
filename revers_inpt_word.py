##############################################################
# Program revers String
# Python 3.2
##############################################################
import sys

__author__ = 'MK'

# global
user_word = ''

# define revers function
def rev(user_word): return user_word[::-1]

# entry point
user_word = (sys.argv[1])
user_word = rev(user_word)
print(user_word)


