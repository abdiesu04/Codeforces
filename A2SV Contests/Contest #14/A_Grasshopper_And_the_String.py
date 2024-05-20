s = input()

vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

jump = 0
init = 1
for ch in s:
    if ch in vowels:
        jump = max(jump, init)
        init = 0
    init += 1
jump = max(jump, init)
print(jump)