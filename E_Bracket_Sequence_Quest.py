s = input()
longest = 0
stack = []
last = -1
res = 0

for i, ch in enumerate(s):
    if ch == "(":
        stack.append(i)
    else:
        if stack:
            stack.pop()
            if stack:
                longest = max(longest, i - stack[-1])
            else:
                longest = max(longest, i - last)
                res += 1
        else:
            last = i

if longest == 0:
    print(0, 1)
else:
    for i in stack:
        if i + longest <= len(s) and s[i + longest] == ")":
            res += 1
    print(longest, res)