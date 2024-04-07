
def angryProfessor(k, a):
    result = ""
    count = 0
    for time in a:
        if time <= 0:
            count += 1
    if count < k:
        result = "YES"
    else:
        result = "NO"
    return result