import math
n , m , a = map(int , input().split())
row = math.ceil(n / a)
col = math.ceil(m / a)
print(row * col)




