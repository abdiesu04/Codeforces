times = int(input())

for _ in range(times):
    n = int(input())
    a = [int(x) for x in input().split()]

    maxim_it = n  

    is_sorted = False
    while not is_sorted and maxim_it > 0:
        is_sorted = True  

        for i in range(n - 1):
            if a[i] > a[i + 1]:
                digits = [int(x) for x in str(a[i])]
                
                a = a[:i] + digits + a[i + 1:]
                n += len(digits) - 1
                is_sorted = False  
                break

        maxim_it -= 1

    if a == sorted(a):
        print("YES")
    else:
        print("NO")