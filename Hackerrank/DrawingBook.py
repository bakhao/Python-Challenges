

def pageCount(n, p):
    result = 0
    minfromStart = p//2
    minfromEnd = (n - p + (1 if n % 2 == 0 else 0)) // 2
    result = min(minfromStart, minfromEnd)
    return result