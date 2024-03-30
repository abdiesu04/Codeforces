# n = int(input())
# cnt = 0
# for i in range(2 ,n+1):
#     res = []
#     d = 2
#     while d * d <= i:
#         while i % d == 0:
#             res.append(d)
#             i //= d
#         d += 1
#     if i > 1:
#         res.append(i)
#     if len(set(res)) == 2:
#         cnt += 1
# print(cnt)


print(set([(1,2), (1,2)]))