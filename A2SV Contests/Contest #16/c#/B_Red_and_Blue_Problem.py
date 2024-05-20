
	
def answer(red, n, blue, m):

    maxim = 0
    cnt = 0
    for i in red:
        cnt += i
        maxim = max(maxim, cnt)

    maxim2 = 0
    cnt = 0

    for i in blue:
        cnt += i
        maxim2 = max(maxim2, cnt)

    print(maxim + maxim2)
    return

t = int(input())



for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    data1 = list(map(int, input().split()))

    answer(data, n, data1, m)


