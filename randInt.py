import random
import sys

__author__ = 'Michal'


# pseudocode
# random integers

# parameter von user einlesen, und check
n = int(sys.argv[1])
m = int(sys.argv[2])


'''
n = int(input('Geben Sie anzahl:')) # anzahl der zahlen
m = int(input('Bereich:')) # bereich
'''


# loops schleife
for i in range(0,n):
    # zufalszahl generieren
    my_number = random.randint(0, m)
    #zufalszahl ausgenen
    print (my_number)


