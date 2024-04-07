from typing import List


def vote_majoritaire(votes: List[int]):
    vote_with_occur = {}
    for vote in votes:
        vote_with_occur[vote] = votes.count(vote)
    vote_with_occur_sorted = dict(sorted(vote_with_occur.items(), key=lambda item: item[1]))
    vote_with_occur_sorted_values = [i for i in vote_with_occur_sorted.values()]
    if vote_with_occur_sorted_values[-2] == vote_with_occur_sorted_values[-1]:
        return None
    return list(vote_with_occur_sorted)[-1]


def findDisappearedNumbers(nums):
    list_with_all_Numbers = list(range(1, len(nums) + 1))
    list_disappearedNumbers = []
    for i in list_with_all_Numbers:
        if i not in nums:
            list_disappearedNumbers.append(i)
    return list_disappearedNumbers
