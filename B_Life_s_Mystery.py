s = input()
while len(s) > 1:
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    s = "".join(stack)
    if len(s) == 1 or s == "".join(stack):
        break
print(s)