# -----------------1337. The K Weakest Rows in a Matrix----------------
def count_1_in_list(liste):
    count = 0
    for i in liste:
        if i == 1:
            count += 1
    return count


def kWeakestRows(mat, k):
    rows_value = {}
    for row, value in enumerate(mat):
        rows_value[row] = count_1_in_list(value)
    dic_kWeakestRows = dict(sorted(rows_value.items(), key=lambda item: item[1]))
    kWeakestRowsList = [i for i in dic_kWeakestRows.keys()]
    return kWeakestRowsList[:k]
