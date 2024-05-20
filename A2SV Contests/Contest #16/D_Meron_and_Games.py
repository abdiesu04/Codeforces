n = int(input())
arr  = list(map(int , input().split()))
dp = [0]* 100001
for i in range(len(arr)):
    dp[i] = arr[i]
for i in range(2, 100001):
    dp[i] = max(dp[i-1], dp[i-2] + dp[i])
print(dp[n])