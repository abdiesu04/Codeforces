t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    n_values = list(map(int, input().split()))
    
    for n in n_values:
        x = arr[0]
        if n >= x:
            print(x - 1, end=" ")
        else:
            print(n, end=" ")
    print()