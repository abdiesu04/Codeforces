


n , a , b , c  = map(int,input().split())
# ribs  = [a,b,c]
# dp = [float('-inf')] * (n + 1)
# dp[0] = 0
# for rib in ribs:
#     for i in range(rib , n + 1):
#         dp[i] = max(dp[i] , dp[i - rib] + 1)
# print(dp[n])



denom = [a,b,c]
denom.reverse()
c = 0

for x in denom:
    if n >= x:
        num = n // x
        n = n - (num * x)
        c += num

print(c)
