n = int(input())
min_price = float('inf')
total_cost = 0
for _ in range(n):
    a, p = map(int, input().split())
    min_price = min(min_price, p)
    total_cost += a * min_price
print(total_cost)