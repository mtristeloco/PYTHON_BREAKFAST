import random

__author__ = 'MK'


# pseudocode
# random integers

# parameter von user einlesen, und check
# n = int(sys.argv[1])
# m = int(sys.argv[2])

# helpfunktion

def help():
    print ("This is the randInt.py help Options:-h... shows this help"
     "Sample:$>randInt.py 5 100 "
     "parameter description:  randInt...program name"
     "                        5... how many randoms"
     "                        100... range, ie between 0...100")


n = int(input('Geben Sie anzahl:')) # anzahl der zahlen
m = int(input('Bereich:')) # bereich

outputfile = (input('Geben Sie die Name der Datei ein:')) #Name der Datei

datei = open (outputfile, "a") # "r", "w", "a"

# loops schleife
for i in range(0,n):
    # zufalszahl generieren
    my_number = random.randint(0, m)
    #zufalszahl ausgebeen
    #print (my_number)

    #schreibe Ergebnis (str umwandelt ins Text!) in die Datei
    datei.write(str(my_number) + '\n')

datei.close()
