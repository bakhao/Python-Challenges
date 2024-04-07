def cutTheSticks(arr):
    numSticks = []
    arrSorted = sorted(arr)
    while arrSorted:
        sizeArrSorted = len(arrSorted)
        numSticks.append(sizeArrSorted)
        minStick = min(arrSorted)
        arrSorted = [x - minStick for x in arrSorted if x != minStick]
    return numSticks
