n = int(input())
if n % 2 != 0:
    print(-1)
else:
    permutation = [0] * n
    for i in range(0, n, 2):
        permutation[i] = i + 2
        permutation[i + 1] = i + 1
    print(' '.join(map(str, permutation)))