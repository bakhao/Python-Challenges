def rotateLeft(d, arr):
    # Calculate the effective rotation count to avoid unnecessary rotations
    index_rotated = d % len(arr)
    # Use slicing to rotate the array in one step
    rotated_arr = arr[index_rotated:] + arr[:index_rotated]
    return rotated_arr
