def solve(n):
    if n%2==1 or n<2:
        return "NO"
    print("YES")
    ans= "AAB"*(n//2)
    return ans
t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))