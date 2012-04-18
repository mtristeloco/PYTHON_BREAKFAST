##############################################################
# Name:     randInt.py
#
# Generate n random numbers in rage from 0 to m and save them
# to given name.txt file
#
# Michal Kalinic
# Python 3.2
# ##############################################################
import random
import sys

__author__ = 'MK'

# global
n = 0
m = 0

def my_help():
    print('''

    This is a help.
    Test

    ''')
    quit()

# entry point
if sys.argv[1] == '-h':
    my_help()
else:
    user_file = sys.argv[3]
    output_file = open(user_file, "a")

# read parameters from user
if len(sys.argv) > 1:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    # loops
    for i in range(0,n):
        my_number = random.randint(0, m)
        output_file.write(str(my_number) + '\n')

output_file.close()