t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt = s.count('1')
    if cnt % 2 != 0:
        print("NO")
        continue
    
    possible = True
    
    if cnt == 2:
        for i in range(len(s) - 1):
            if s[i] == '1' and s[i+1] == '1':
                possible = False
                break
    
    if possible:
        print("YES")
    else:
        print("NO")