from collections import defaultdict


n = int(input())
heights = list(map(int, input().split()))
stack = []
frequency = defaultdict(int)


for i in range(n+1):
    while stack and (i == n or heights[stack[-1]] >= heights[i]):
        num = stack.pop()
        left_boundary = stack[-1] if stack else -1
        right_boundary = i
        size = (right_boundary - num) + (num - left_boundary - 1)
        frequency[size] = max(heights[num],frequency[size])
    stack.append(i)
    


res = []
for i in heights:
    res.append(frequency[i])
print(sorted)


    
# from collections import defaultdict

# n = int(input())
# heights = list(map(int, input().split()))
# stack = []
# frequency = defaultdict(int)

# for i in range(n+1):
#     while stack and (i == n or heights[stack[-1]] > heights[i]):
#         num = stack.pop()
#         left_boundary = stack[-1] if stack else -1
#         right_boundary = i
#         size = (right_boundary - left_boundary - 1)  # Fix the size calculation
#         frequency[size] = max(heights[num], frequency[size])  # Store the maximum height for each size
#     stack.append(i)

# # Update frequency dictionary to store maximum strength for each size
# for size in frequency:
#     frequency[size] = max(frequency[size], frequency[size+1])

# # Generate the output
# output = []
# for i in range(1, n+1):
#     output.append(frequency[i])
# print(' '.join(map(str, output)))


