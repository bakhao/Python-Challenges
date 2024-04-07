
def getMoneySpent(keyboards, drives, b):
    maxSpend = -1
    list_costs = []
    for keyboard in keyboards:
        for drive in drives:
            totalCost = keyboard + drive
            if b >= totalCost:
                list_costs.append(totalCost)
    list_costs_sorted = sorted(list_costs)
    if list_costs_sorted:
        maxSpend = list_costs_sorted[-1]
    else:
        maxSpend = -1
    return maxSpend