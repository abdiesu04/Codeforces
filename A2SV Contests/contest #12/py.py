# from collections import deque

# def bfs(graph, start):
#     # Initialize the visited set and queue
#     visited = set()
#     queue = deque([start])
    
#     while queue:
#         node = queue.popleft()
#         # Process the node
#         process_node(node)
        
#         # Mark the node as visited
#         visited.add(node)
        
#         # Explore the neighbors of the current node
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)

# def process_node(node):
#     # Implement your logic to process each node
#     # Here you can perform the necessary operations
#     # based on the requirements of the Codeforces problem
#     pass

# # Example usage:
# # Define the graph as an adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'E'],
#     'D': ['B'],
#     'E': ['C', 'F'],
#     'F': ['E']
# }

# start_node = 'A'
# bfs(graph, start_node)



# from collections import deque

# def shortest_path(graph, start, target):
#     # Initialize the visited set, queue, and distance dictionary
#     visited = set()
#     queue = deque([(start, 0)])
#     distance = {start: 0}
    
#     while queue:
#         node, dist = queue.popleft()
        
#         if node == target:
#             return dist
        
#         visited.add(node)
        
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append((neighbor, dist + 1))
#                 distance[neighbor] = dist + 1
    
#     # If the target node is unreachable
#     return -1

# # Example usage:
# # Define the graph as an adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'E'],
#     'D': ['B'],
#     'E': ['C', 'F'],
#     'F': ['E']
# }

# start_node = 'A'
# target_node = 'F'
# shortest_dist = shortest_path(graph, start_node, target_node)

# if shortest_dist != -1:
#     print(f"Shortest distance from {start_node} to {target_node} is {shortest_dist}")
# else:
#     print(f"No path found from {start_node} to {target_node}")