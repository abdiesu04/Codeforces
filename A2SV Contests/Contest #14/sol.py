def dfs(i, capacity):
    if i == len(profit):
        return 0

    maxProfit = dfs(i+1, capacity)
    newCap = capacity - weight[i]
    if newCap >= 0:
        p = profit[i] + dfs(i+1, newCap)
        maxProfit = max(maxProfit, p)
    return maxProfit

capacity = 8
profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]

print(dfs(0, capacity))