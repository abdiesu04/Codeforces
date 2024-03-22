n , t = map(int , input().split())
nums = list(map(int , input().split()))
nums.sort()
cnt = 0 
sm = 0
for i in range(len(nums)):
    sm += nums[i]
    if sm <= t:
        cnt += 1
print(cnt)
        