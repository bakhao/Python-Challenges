
# scherlock and squares
import math


def squares(a, b):
    # Write your code here
    firstSquare = math.sqrt(a)
    lastSquare = math.sqrt(b)
    numSquareInteger = (math.floor(lastSquare) - math.ceil(firstSquare)) + 1
    return numSquareInteger
