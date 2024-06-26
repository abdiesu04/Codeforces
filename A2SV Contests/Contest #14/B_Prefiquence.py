# You are given two binary strings a
#  and b
# . A binary string is a string consisting of the characters '0' and '1'.

# Your task is to determine the maximum possible number k
#  such that a prefix of string a
#  of length k
#  is a subsequence of string b
# .

# A sequence a
#  is a subsequence of a sequence b
#  if a
#  can be obtained from b
#  by the deletion of several (possibly, zero or all) elements.

# Input
# The first line consists of a single integer t
#  (1≤t≤104
# ) — the number of test cases.

# The first line of each test case contains two integers n
#  and m
#  (1≤n,m≤2⋅105
# ) — the length of string a
#  and the length of string b
# , respectively.

# The second line of each test case contains a binary string a
#  of length n
# .

# The third line of each test case contains a binary string b
#  of length m
# .

# It is guaranteed that the sum of values n
#  over all test cases does not exceed 2⋅105
# . Similarly, the sum of values m
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output a single number — the maximum k
# , such that the first k
#  characters of a
#  form a subsequence of b
# .

# Example
# inputCopy
# 6
# 5 4
# 10011
# 1110
# 3 3
# 100
# 110
# 1 3
# 1
# 111
# 4 4
# 1011
# 1111
# 3 5
# 100
# 11010
# 3 1
# 100
# 0
# outputCopy
# 2
# 2
# 1
# 1
# 3
# 0
# Note
# In the first example, the string '10
# ' is a subsequence of '1110
# ' but the string '100
# ' is not. So the answer is 2
# .

# In the fifth example, a
# ='100
# ', b
# ='11010
# ', whole string a
#  is a subsequence of string b
# . So the answer is 3
# .

# In the sixth example, string b
#  does not contain '1
# ' so the answer is 0
# .










t = int(input())
for _ in range(t):
    n , m = map(int , input().split())
    a = input()
    b = input()
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
        j += 1  
    print(i)