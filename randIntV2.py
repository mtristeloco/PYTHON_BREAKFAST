__author__ = ''
# randInt.py

import random
import sys


__author__ = 'MK'


# all my comments with #SAP:

# pseudocode
# random integers

# parameter von user einlesen, und check
n = int(sys.argv[1])
m = int(sys.argv[2])

def my_help():
    print("XXXXX")

my_help()

n = int(input('Geben Sie anzahl:')) # how many numbers have to be gene  #SAP: please all comments and variable names in English
m = int(input('Bereich:')) # bereich

outputfile = (input('Geben Sie die Name der Datei ein:')) # Name of the output File

datei = open (outputfile, "a") # "r", "w", "a"

# loops schleife
for i in range(0,n):
    # zufalszahl generieren
    my_number = random.randint(0, m)
    #zufalszahl ausgebeen
    #print (my_number)

    #schreibe Ergebnis in die Datei
    datei.write(str(my_number) + '\n')

datei.close()
#SAP: TODOs
# write a nice header to this program at the beginning (Name of program, parameters, compiler used, etc)

