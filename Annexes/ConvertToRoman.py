
def convertToRoman(num):
    result = ""
    arabics_to_roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    list_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    for number in list_numbers:
        while num >= number:
            result += arabics_to_roman[number]
            num -= number
            print("num ", num)
    return result


def find_closest(my_list, target):
    # Use the min function with a key that calculates the absolute difference
    # between each number and the target
    closest_num = min(my_list, key=lambda x: abs(x - target))
    return closest_num