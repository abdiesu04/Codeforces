profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
n = len(profit)
capacity = 8
mx = 0
memo = [[-1] * (capacity + 1) for _ in range(n)]

def backtrack(i, val, capacity):
    global mx
    if i == n or capacity == 0:  # Termination condition corrected
        mx = max(mx, val)
        return

    if memo[i][capacity] != -1:
        return memo[i][capacity]

    if weight[i] > capacity:
        memo[i][capacity] = backtrack(i + 1, val, capacity)
        return memo[i][capacity]

    backtrack(i + 1, val + profit[i], capacity - weight[i])
    memo[i][capacity] = backtrack(i + 1, val, capacity)
    return memo[i][capacity]

backtrack(0, 0, capacity)
print(mx)