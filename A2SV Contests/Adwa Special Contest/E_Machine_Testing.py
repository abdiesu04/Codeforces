res = [1]
for i in range(20):
    if res[i] < 10:
        res.append(res[i] * 2)
    else:
        n = res[i]
        p = 1
        while n > 0:
            d = n %10
            if d != 0:
                p *= d
            n //= 10
        res.append(res[i] + p)

print(res)