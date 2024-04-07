def hourglassSum(arr):
    list_sumHourGlass = []
    somme = 0
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
                    somme = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                    list_sumHourGlass.append(somme)
    return max(list_sumHourGlass)
