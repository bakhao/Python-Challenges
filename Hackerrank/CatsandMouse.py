
def catAndMouse(x, y, z):
    result = " "
    if abs(x - z) < abs(y - z):
        result = 'Cat A'
    elif abs(x - z) > abs(y - z):
        result = 'Cat B'
    else:
        result = 'Mouse C'
    return result