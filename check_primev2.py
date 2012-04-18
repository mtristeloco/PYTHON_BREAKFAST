##############################################################
# Name:     check_prime
#
# The program checks if the given number is prime and if not
# then gives the number with which you can divide it
#
# Michal Kalinic
# Python 3.2
# ##############################################################
import sys
import time

__author__ = 'Michal'

running_time = time.time()

x = int(sys.argv[1])

def isprime(x):
    x = abs(int(x))                             # prime numbers can only be positive absolute number
    if x < 2:                                   # prime number cannot be les then 2
        return "Less 2", False
    elif x == 2:                                # 2 is the 1-th prime number
        return True
    elif x % 2 == 0:
        return False
    else:                                       # the actual proof
        for n in range(3, int(x**0.5)+2, 2):
            if x % n == 0:
                return n, False
        return True

print (x, isprime(x))                           # print the result
print (time.time() - running_time, 'seconds')   # print the time

