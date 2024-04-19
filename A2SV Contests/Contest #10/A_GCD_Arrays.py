from collections import defaultdict
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        new_graph = defaultdict(list)
        for i in range(len(graph)):
            new_graph[i] = graph[i]
        # print(new_graph)
            
        visited = [0 for _ in range(len(graph))]

        col = 1
        def dfs(node , visited):
            visited[node] = col * -1

            for child in graph[node]:
                if visited[child] != 0 and visited[child] == col:
                    return False
                dfs(child, visited)
                print(visited[child], col)
            return True

        return dfs(0 , visited)

        


sol = Solution()
print(sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))