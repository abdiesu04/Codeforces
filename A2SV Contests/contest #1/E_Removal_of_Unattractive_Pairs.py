orda = ord('a')

def solve():
    n = int(input())
    cnt = [0] * 26
    for c in input():
        cnt[ord(c) - orda] += 1
    mx = max(cnt)
    print(max(n % 2, 2 * mx - n))


for _ in range(int(input())):
    solve()