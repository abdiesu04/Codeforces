t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    xs  = [0]
    ys  = [0]
    for _ in range(c):
        x , y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    xs.append(a + 1)
    ys.append(b + 1)
    xs.sort()
    ys.sort()
    xss , yss  = [ ], []
    for i in range(1,len(xs)):
        xss.append(xs[i] - xs[i-1])
        yss.append(ys[i] - ys[i-1])
    print(max(xss) * max(yss))