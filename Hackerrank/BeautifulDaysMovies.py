
def beautifulDays(i, j, k):
    count = 0
    for number in range(i, j+1):
        calculDay = abs(number - reverseDigit(number))/ k
        if calculDay.is_integer():
            count += 1
    return count


def reverseDigit(number):
    result = ""
    numberReversed = list(str(number))[::-1]
    if numberReversed[0] != '0':
        result = ''.join(numberReversed)
    else:
        result = ''.join(numberReversed[1:])
    return int(result)