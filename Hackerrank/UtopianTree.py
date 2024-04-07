
def utopianTree(n):
    height = 0
    for period in range(n+1):
        if period%2 == 0:
            height += 1
        else:
            height *= 2
    return height