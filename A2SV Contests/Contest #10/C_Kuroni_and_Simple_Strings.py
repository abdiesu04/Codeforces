data = input()
res = [0] * len(data)
first = -1
last  = -1
for i in range(0, len(data)):
    if data[i] == '(':
        first = i
        break
for i in range(len(data) - 1, -1, -1):
    if data[i] == ')':
        last = i
        break

while first < last:
    if data[first] == '(' and data[last] == ')':
        res[first] = 1
        res[last] = 1
    first += 1
    last -= 1
ans = []
for i in range(len(res)):
    if res[i] == 1:
        ans.append(i+1)
# if not ans:
#     print(0)
# else:
#     print(1)
#     print(len(ans))
#     print(*ans)
def check_parentheses_order(string):
    stack = []
    f = 0
    
    for char in string:
        if char == '(' and f == 0:
            return False
        elif char == ')':
            f += 1
    
    return True



if check_parentheses_order(data):
     print(0)
else:
    print(1)
    print(len(ans))
    print(*ans)



