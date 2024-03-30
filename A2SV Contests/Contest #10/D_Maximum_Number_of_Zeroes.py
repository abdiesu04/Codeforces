from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ratios = defaultdict(int)
zeros = 0

for i in range(n):
    if a[i] == 0 and b[i] == 0:
        zeros += 1
    elif a[i] != 0 and b[i] != 0:
        if (a[i] < 0 and b[i] > 0) or (a[i] > 0 and b[i] < 0):
            ratios[(abs(a[i]), abs(b[i]), -1)] += 1
        else:
            ratios[(abs(a[i]), abs(b[i]), 1)] += 1

if ratios:
    print(max(max(ratios.values()) + zeros, zeros) + 1)
else:
    print(zeros)