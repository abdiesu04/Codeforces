from collections import defaultdict

def check(ch, mp):
    for i in range(ord('a'), ord(ch)):
        if mp[chr(i)] > 0:
            return False
    return True

s = input()

mp = defaultdict(int)
for ch in s:
    mp[ch] += 1

t = ""
st = []
for ch in s:
    while st and check(st[-1], mp):
        t += st.pop()
        
    st.append(ch)
    mp[ch] -= 1

while st:
    t += st.pop()

print(t)