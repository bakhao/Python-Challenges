
def pickingNumbers(a):
    # Write your code here
    frequency_numbers = {}
    maximumLength = 0
    for number in a:
        count = a.count(number)
        frequency_numbers[number] = count
    for number in frequency_numbers:
        current_length = frequency_numbers[number]
        if number + 1 in frequency_numbers:
            current_length += frequency_numbers[number + 1]
        maximumLength = max(maximumLength, current_length)
    return maximumLength

