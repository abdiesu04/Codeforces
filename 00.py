s1 = input()
s2  = input()

start = 0
end = 0

for i in range(len(s2)):
    if s2[i] == s1[0]:
        start = i
for i in range(len(s2)):

    if s2[i] == s1[-1]:
        end = i
        break
print(max(start, len(s2) - end - 1) if s1 != s2 else 0)
print(start, end)