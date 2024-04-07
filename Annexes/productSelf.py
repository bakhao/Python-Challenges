
def sort_array(source_array):

    pass



def prod(nums):
   res = 1
   for i in nums:
    res *= i
   return res

def sort_array(source_array):

    liste_odd = []
    for i in source_array:
        if i%2 != 0:
            liste_odd.append(i)

    liste_odd.sort()
    return liste_odd


liste = [1,2,3,4]