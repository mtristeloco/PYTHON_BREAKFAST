##############################################################
# Name:     pascal_triangle_symbolic.py
#
# Draw symbolic Pascal Triangle
#
# Michal Kalinic
# Python 3.2
# ##############################################################
import sys

__author__ = 'Michal'

character = sys.argv[1]
n = int(sys.argv[2])
draw = ''
def pascal_triangel():
    for l in range(1, n):
        draw_line = draw + ' '
    for i in range(0, n):
        draw_line = draw[1:]
        draw_line = draw + ' ' + character
        print (draw)

pascal_triangel()

# Why I cannot print it?

'''
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line
'''
