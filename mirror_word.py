##############################################################
# mirror_word.py
# return reversed the word given by the user
#
# Michal Kalinic
# Python 3.2
###############################################################
import sys

__author__ = 'MK'

# global
user_word = ''

# define revers function rev
def rev(user_word): return user_word[::-1]
''' [:] returns the input defined
by the first character, [::-1] make the same in reversed form '''

# entry point
user_word = (sys.argv[1])
user_word = rev(user_word)
print(user_word)


