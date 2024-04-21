from collections import defaultdict
import heapq

n , k = map(int,input().split())
graph = defaultdict(list)
indegree = [0] * n
for i in range(k):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1
q = []
for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(q, i)
print('q',q)
ans = []
while q:
    u = heapq.heappop(q)
    
    ans.append(u+1)
    print('a')
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(q, v)
            print('q',q)
if len(ans) == n:
    print(*ans)
else:    
    print(-1)