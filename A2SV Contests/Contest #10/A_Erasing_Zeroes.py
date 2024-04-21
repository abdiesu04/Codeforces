t = int(input())
for _ in range(t):
    s = input()
    first , last = 0 , 0
    for i in range(len(s)):
        if s[i] == '1':
            first = i
            break

    for i in range(len(s)):
        if s[i] == '1':
            last = i

    cnt = 0
    # print(first , last)
    for i in range(first , last):
        if s[i] == '0':
            cnt += 1
    print(cnt)