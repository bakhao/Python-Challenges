
def icecreamParlor(m, arr):
    # Write your code here
    indicesCost = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == m:
                indicesCost.append(i+1)
                indicesCost.append(j+1)
    return indicesCost