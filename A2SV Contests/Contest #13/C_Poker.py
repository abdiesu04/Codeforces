import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(x) for x in input().split()]
    ans = 0
    bonuses = []
    for i in s:
        if i > 0:
            heapq.heappush(bonuses, -i) 
        else:
            if bonuses:
                ans -= heapq.heappop(bonuses)
    print(ans)