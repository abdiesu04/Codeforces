from collections import defaultdict


t = int(input())
width = list(map(int, input().split()))
persons = input()
res = ''
mapp = defaultdict(int)

for i in persons:
    if i == '1':
        temp = max(width)
        if mapp[temp] < 2:
            res += '1'
            mapp[temp] += 1