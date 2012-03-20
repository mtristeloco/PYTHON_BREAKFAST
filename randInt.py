import random
import sys

__author__ = 'Michal'


# pseudocode
# random integers

# parameter von user einlesen, und check
n = int(sys.argv[1])
m = int(sys.argv[2])
outputfile = (input('Geben Sie die Name der Datei ein:'))

'''
n = int(input('Geben Sie anzahl:')) # anzahl der zahlen
m = int(input('Bereich:')) # bereich
'''

fobj = open (outputfile, "w")

# loops schleife
for i in range(0,n):
    # zufalszahl generieren
    my_number = random.randint(0, m)
    #zufalszahl ausgenen
'''
    print (my_number)
'''
    fobj.write('my_number')

fobj.close()
