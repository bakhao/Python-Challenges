import timeit
from collections import OrderedDict
from itertools import permutations
import time
import string


def findEvenNumbers(digits):
    digits_perm = permutations(digits, 3)
    digits_sorted = []
    liste_entier = []
    number_transformed = 0
    for i in list(digits_perm):
        if i[0] != 0:
            number_transformed = tranform_tuple_to_number(i)
            liste_entier.append(number_transformed)
    for number in liste_entier:
        if number % 2 == 0:
            digits_sorted.append(number)
    return list(sorted(set(digits_sorted)))


def tranform_tuple_to_number(tuple):
    number = ""
    for i in tuple:
        number += str(i)
    return int(number)


def findTheDistanceValue(arr1, arr2, d):
    st = time.time()
    distance = 0
    result = 0
    list_arr1 = []
    for i in arr1:
        for j in arr2:
            distance = abs(i - j)
            if distance <= d:
                list_arr1.append(i)
    list_arr1 = list(set(list_arr1))
    result = [i for i in arr1 if i not in list_arr1]
    et = time.time()
    delta_time = et - st
    print('Execution time:', delta_time * 1000, 'milliseconds')
    return len(result)


def sum_Square_difference(n):
    st = time.time()
    difference = 0
    sum_square = sum([i ** 2 for i in range(1, n + 1)])
    square_sum = sum([i for i in range(1, n + 1)]) ** 2
    difference = square_sum - sum_square
    et = time.time()
    delta_time = et - st
    print('Execution time:', delta_time * 1000, 'milliseconds')
    return difference


def countCharacters(words, chars):
    sum_len_words = 0
    for word in words:
        if checkWord_in_word(word, chars):
            sum_len_words += len(word)
    return sum_len_words


def checkWord_in_word(word1, word2):
    n = len(word1)
    size_target = 0
    for i in word1:
        if i in word2:
            size_target += 1
    return size_target == n


def firstUniqChar(s: str):
    index_firstUniqChar = 0
    dic_char_uniq = {}
    list_index_char = []
    for i, j in enumerate(s):
        if s.count(j) == 1:
            list_index_char.append(j)
            index_firstUniqChar = i
            break
        else:
            index_firstUniqChar = -1
    return index_firstUniqChar


# nums1 = [4,1,2]
# nums2 = [1,3,4,2]

def nextGreaterElement(nums1: list, nums2: list):
    output = []
    j = 0
    for i in nums1:
        for j in nums2[nums2.index(i):]:
            if j > i:
                output.append(j)
                break
        else:
            output.append(-1)
    return output


def nextGreatestLetter(letters, target):
    next_greater_item = ""
    if target not in letters:
        letters.append(target)
        letters_with_target = sorted(letters)
        next_greater_item = letters_with_target[letters_with_target.index(target) + 1]
    else:
        letters_with_target = sorted(letters)
        next_greater_item = letters_with_target[letters_with_target.index(target) + 1]
    return next_greater_item


# ----------------1544. Make The String Great-----*/
# s = "leEeetcode"

def makeGood(s: str):
    good_string = ""
    res = " "
    i = 0
    while i < len(s) - 1:
        if s[i] != s[i + 1] and (s[i] == s[i + 1].upper() or s[i] == s[i + 1].lower()):
            good_string = s[:i] + s[i + 2: len(s)]
            i = 0
        else:
            i += 1
    return good_string


# ---------819. Most Common Word--------------#

def mostCommonWord(paragraph, banned):
    paragraph_without_punction = paragraph.translate(str.maketrans('', '', string.punctuation))
    paragraph_without_banned = " "
    words = {}
    for i in banned:
        paragraph_without_banned = paragraph_without_punction.replace(i, "")

    list_paragraph = paragraph_without_banned.lower().split(" ")
    for word in list_paragraph:
        words[word] = list_paragraph.count(word)
    words_sorted = OrderedDict(sorted(words.items(), key=lambda x: x[1]))
    if '' in words_sorted:
        del words_sorted['']

    print(words_sorted)
    print("last item ", list(words_sorted)[-1])
    return list(words_sorted)[-1]


# ------2200. Find All K-Distant Indices in an Array-------------------

def findKDistantIndices(nums, key, k):
    list_index_values_key = []
    list_k_distant_Indices = []
    for i, value in enumerate(nums):
        if nums[i] == key:
            list_index_values_key.append(i)
    for i in range(len(nums)):
        for j in list_index_values_key:
            if abs(i - j) <= k and nums[j] == key:
                list_k_distant_Indices.append(i)
    list_k_distant_Indices_sorted = sorted(list(set(list_k_distant_Indices)))
    return list_k_distant_Indices_sorted


# -----------------657. Robot Return to Origin--------

def judgeCircle(moves):
    origin = (0, 0)
    target = (0, 0)
    x, y = 0, 0
    for i in moves:
        if i == 'R':
            x += 1
        elif i == 'L':
            x -= 1
        elif i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        else:
            x, y = 0, 0
    target = (x, y)
    print(f"target {target}")
    if target == origin:
        return True
    else:
        return False


