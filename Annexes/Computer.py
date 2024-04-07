def save(sizes, hd):
    # your code here
    count = 0
    sum = 0
    for i in sizes:
        sum += i
        if sum <= hd:
            count += 1
        else:
            break
    return count


def dont_give_me_five(start,end):
    count = 0
    liste = [str(i) for i in range(start, end+1)]
    res = []
    for j in liste:
        if not containsFive(j):
            res.append(j)

    return len(res)

def containsFive(digit):
    if "5" in digit:
        return True
    else:
        return False