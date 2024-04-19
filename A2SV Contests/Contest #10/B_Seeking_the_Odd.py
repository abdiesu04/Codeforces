def has_single_one(n):
    binary = bin(n)
    count = binary.count('1')
    return count == 1



t = int(input())
for _ in range(t):
    n = int(input())
    print("NO" if has_single_one(n)  else "YES")
    
