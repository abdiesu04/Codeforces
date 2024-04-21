n = int(input())
chest = 0
back = 0
bic = 0
arr = list(map(int, input().split()))
for i in range(n):
    if i % 3 == 0:
        chest += arr[i]
    elif i % 3 == 1:
        bic += arr[i]
    else:
        back += arr[i]
print("chest" if chest > bic and chest > back else "biceps" if bic > chest and bic > back else "back")