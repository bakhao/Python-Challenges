
# counting Sort 1
def countingSort(arr):
    # Write your code
    result = [0 for i in list(range(0, 100))]
    for i, value in enumerate(arr):
        result[value] += 1
    return result