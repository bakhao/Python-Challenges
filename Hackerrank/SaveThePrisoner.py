
def saveThePrisoner(n, m, s):
    # Write your code here
    numCurrentChair = (m + s - 1) % n
    if numCurrentChair == 0:
        numCurrentChair = n
    return numCurrentChair
