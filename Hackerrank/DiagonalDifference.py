def diagonalDifference(arr):
    # Write your code here
    result = 0
    diag_right_to_left = []
    diag_left_to_right = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                diag_left_to_right.append(arr[i][j])
            if j == len(arr) - 1 - i:
                diag_right_to_left.append(arr[i][j])
    result = abs(sum(diag_left_to_right) - sum(diag_right_to_left))
    return result
