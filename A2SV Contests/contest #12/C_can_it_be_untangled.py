import math

stack = []

nums = list(input().strip())

while nums:
    x = nums.pop()

    if stack:
        if stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
    else:
        stack.append(x)

if stack:
    print("No")
else:
    print("Yes")