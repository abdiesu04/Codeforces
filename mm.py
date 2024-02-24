# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))
#     t = sorted(s)
#     for i in range(n):
#         if s[i] != t[-1]:
#             s[i] = s[i] - t[-1]
#         else:
#             s[i] = s[i] - t[-2]
#     print(*s)


#     #liya
# s = input()
# m = int(input())
# queries = []

# for _ in range(m):
#     queries.append(list(map(int, input().split())))

# pref = [0]
# for indx in range(len(s) - 1):
#     if s[indx] == s[indx + 1]:
#         pref.append(pref[-1] + 1)
    
#     else:
#         pref.append(pref[-1])


# for left, right in queries:
#     print(pref[right - 1] - pref[left - 1])


# hate

#  n = int(input())
#     time = sorted(map(int, input().split()))

#     ans = waitTime = 0
#     for i in range(n):
#         if waitTime <= time[i]:
#             ans += 1
#             waitTime += time[i]
    
#     print(ans)