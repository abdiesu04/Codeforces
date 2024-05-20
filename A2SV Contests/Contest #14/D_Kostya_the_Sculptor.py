# def pr_binary(num):
#     for i in range(4, -1, -1):
#         # print(num>>1)
#         print((num >> i) & 1)
     
# # pr_binary(10)
# num = 15
# cnt  = 0
# for i in range(31,-1,-1):
#     if num & (1<<i):
#         cnt += 1
# print(bin(ord("A")))   
# print(bin(ord("a")))   
# # print(chr(ord('A') | (1 << 5)))
# # print(chr(ord('a') & (~(1 << 5))))
# # print(chr(ord('C') | ord(' ')))
# def grayCode(n):
#     v = []
#     for i in range(1 << n):
#         v.append(i ^ (i >> 1))
#     return v
# print(grayCode(5))

print(9&7)