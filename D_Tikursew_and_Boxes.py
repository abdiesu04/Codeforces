from collections import deque

n = int(input())
stack = []
counter = 0
next_box = 1

for _ in range(2*n):
    command = input().split()
    if command[0] == "add":
        stack.append(int(command[1]))
        next_box = command[1] if command[1] > next_box else next_box
    else:
        if stack and stack[-1] == next_box:
            stack.pop()
        else:
            if stack:
                stack.clear()
                counter += 1
        next_box += 1

print(counter)