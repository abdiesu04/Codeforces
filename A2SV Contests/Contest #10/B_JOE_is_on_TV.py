n = int(input())
res = 0
for i in range(n , 0 , -1):
    # print( 1 , '/' , i)
    res += 1 / i
print("{:4f}".format(res))
