
def sockMerchant(n, ar):
    sockValue = 0
    listSock = []
    pairs_Socks = {}
    for stock in ar:
        pairs_Socks[stock] = ar.count(stock)
    for values in pairs_Socks.values():
        listSock.append(values//2)
    sockValue = sum(listSock)
    return sockValue
