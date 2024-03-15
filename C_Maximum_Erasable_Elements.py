n = int(input())
a = list(map(int, input().split()))
a.append(1005)  # append a large number at the end to handle the last sequence
max_erase = 0
count = 0
for i in range(1, len(a)):
    if a[i] == a[i-1] + 1:
        count += 1
    else:
        max_erase = max(max_erase, count - 1 if count > 0 else 0)  # subtract 1 because we need at least one element to infer the others
        count = 0
print(max_erase)