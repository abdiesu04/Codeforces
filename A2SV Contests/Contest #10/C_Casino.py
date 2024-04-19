from math import gcd

# def lcm(a, b):
#     return abs(a*b) // gcd(a, b)

def reduce(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n

n = int(input())
arr = list(map(int, input().split())) 
base = reduce(arr[0])

for i in range(1, len(arr)):
    if reduce(arr[i]) != base:
        print("No")
        break
else:
    print("Yes")