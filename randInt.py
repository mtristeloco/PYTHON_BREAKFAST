# randInt.py
import random
import sys


__author__ = 'MK'


# all my comments with #SAP:

# pseudocode
# random integers



#global
n = 0
m = 0
outputfile = ''


# entry point
def main():
    # parameter von user einlesen, und check
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            my_help()
        else:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
            outputfile = sys.argv[3]
            random_generator()


################################################################
# Function generates the numbers
# Parameters: none
# Return value: none
################################################################
# entry point
def main():
    def random_generator():
        if n == 0:
            n = int(input('Geben Sie anzahl:')) # how many numbers have to be gene  #SAP: please all comments and variable names in English
        if m == 0:
            m = int(input('Bereich:')) # bereich

        if outputfile == '':
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

def my_help():
    print('''

    This is a help.
    Test

    ''')


if __name__ == '__main__':
    main()