# You are given a 1-indexed array of n
#  integers, a
# , and an integer z
# . You can do the following operation any number (possibly zero) of times:

# Select a positive integer i
#  such that 1≤i≤n
# . Then, simutaneously set ai
#  to (aiorz)
#  and set z
#  to (aiandz)
# . In other words, let x
#  and y
#  respectively be the current values of ai
#  and z
# . Then set ai
#  to (xory)
#  and set z
#  to (xandy)
# .
# Here or
#  and and
#  denote the bitwise operations OR and AND respectively.

# Find the maximum possible value of the maximum value in a
#  after any number (possibly zero) of operations.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). Description of the test cases follows.

# The first line of each test case contains two integers n
#  and z
#  (1≤n≤2000
# , 0≤z<230
# ).

# The second line of each test case contains n
#  integers a1
# ,a2
# ,…
# ,an
#  (0≤ai<230
# ).

# It is guaranteed that the sum of n
#  over all test cases does not exceed 104
# .

# Output
# For each test case, print one integer — the answer to the problem.

# Example
# inputCopy
# 5
# 2 3
# 3 4
# 5 5
# 0 2 4 6 8
# 1 9
# 10
# 5 7
# 7 15 30 29 27
# 3 39548743
# 10293834 10284344 13635445
# outputCopy
# 7
# 13
# 11
# 31
# 48234367
# Note
# In the first test case of the sample, one optimal sequence of operations is:

# Do the operation with i=1
# . Now a1
#  becomes (3or3)=3
#  and z
#  becomes (3and3)=3
# .
# Do the operation with i=2
# . Now a2
#  becomes (4or3)=7
#  and z
#  becomes (4and3)=0
# .
# Do the operation with i=1
# . Now a1
#  becomes (3or0)=3
#  and z
#  becomes (3and0)=0
# .
# After these operations, the sequence a
#  becomes [3,7]
# , and the maximum value in it is 7
# . We can prove that the maximum value in a
#  can never exceed 7
# , so the answer is 7
# .

# In the fourth test case of the sample, one optimal sequence of operations is:

# Do the operation with i=1
# . Now a1
#  becomes (7or7)=7
#  and z
#  becomes (7and7)=7
# .
# Do the operation with i=3
# . Now a3
#  becomes (30or7)=31
#  and z
#  becomes (30and7)=6
# .
# Do the operation with i=5
# . Now a5
#  becomes (27or6)=31
#  and z
#  becomes (27and

import sys

N = 1e05 + 10

def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        maxn = 0
        for i in range(n):
            maxn = max(maxn, arr[i] | m)
        
        print(maxn)

if __name__ == "__main__":
    main()
