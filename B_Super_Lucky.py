from collections import Counter, defaultdict


n = input()

if n[0] == '4' or n[0] == '7':
    while True:
        s = str(n)
        mapp = Counter(s)
        if '7' in s and '4' in s and len(mapp) == 2 and mapp['4'] == mapp['7']:
            print(s)
            break 
        n = int(n)
        n += 1
else:
    n = input()
    if n.count('4') == n.count('7') and len(set(n)) == 2:
        print(n)
    else:
        t = len(n) //2 
        if len(n) % 2 == 0:
            fours = t * '4'
            sevens = t * '7'
            print(fours+sevens)
        else:
            fours = t +1 * '4'
            sevens = t + 1 * '7'
            print(fours+sevens)


    