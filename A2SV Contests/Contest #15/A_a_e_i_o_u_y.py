n = int(input())
vowels = 'aeiouy'
s = input()
ans  = s[0]
for i in range(1,len(s)):
    if s[i] not in vowels or s[i-1] not in vowels:
        ans += s[i]
print(ans)