import itertools


def gameOfThrones(s):
    # Write your code here
    res = "YES"
    count = 0
    freq_word = {}
    for char in s:
        freq_word[char] = s.count(char)
    for value in freq_word.values():
        if value % 2 != 0:
            count += 1
        if count > 1:
            res = "NO"
    return res
