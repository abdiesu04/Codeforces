t = int(input())

for _ in range(t):
    n = int(input())

    sum = 0
    for i in range(1, n + 1):
        sum += (i * 2 - 1) * i

    op = n + n - 1
    if n > 2:
        op += 1

    print(sum, op)

    for i in range(1, n + 1):
        print(1, i, end=" ")
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

    for i in range(1, n):
        print(2, i, end=" ")
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

    if n > 2:
        print(1, 1, end=" ")
        for j in range(1, n + 1):
            print(j, end=" ")
        print()