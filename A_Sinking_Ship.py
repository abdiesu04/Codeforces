n = int(input())

rats = []
womenAndChildren = []
men = []
captain = []
output = []

for _ in range(n):
    name, status = input().split()
    
    if status == "rat":
        rats.append(name)
    elif status == "woman" or status == "child":
        womenAndChildren.append(name)
    elif status == "man":
        men.append(name)
    else:
        captain.append(name)

output = rats + womenAndChildren + men + captain

for name in output:
    print(name)