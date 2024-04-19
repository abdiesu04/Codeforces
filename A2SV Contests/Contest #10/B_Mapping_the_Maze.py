n, m = map(int, input().split())
degrees = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    degrees[x] += 1
    degrees[y] += 1

count1 = degrees.count(1)
count2 = degrees.count(2)
countn1 = degrees.count(n - 1)

if count1 == 2 and count2 == n - 2:
    print("bus topology")
elif count2 == n:
    print("ring topology")
elif count1 == n - 1 and countn1 == 1:
    print("star topology")
else:
    print("unknown topology")