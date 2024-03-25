res = [1]
for i in range(10):
    if res[i] < 10:
        res.append(res[i] * 2)

print(res)