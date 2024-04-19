from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    divs = defaultdict(int)
    for num in arr:
        d = 2
        while d * d <= num:
            while num % d == 0:
                divs[d] += 1
                num //= d
            d += 1
        if num > 1:
            divs[num] += 1
    # print(divs)
    flag = True
    for i in divs.items():
        if i[1] % n != 0:
            flag = False
    print("YES" if flag else "NO")



