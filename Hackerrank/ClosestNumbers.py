

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    arr_pairs = []
    minDifference = 1000000000000000
    for i in range(0, len(arr) - 1):
        if minDifference > abs(arr[i] - arr[i+1]):
            minDifference = abs(arr[i] - arr[i+1])
            arr_pairs.append((arr[i], arr[i+1]))
    arr_pairs = []
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) == minDifference:
            arr_pairs.extend([arr[i], arr[i + 1]])
    return arr_pairs