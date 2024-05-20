# You are given an integer n
# . You choose n
#  cells (x1,y1),(x2,y2),…,(xn,yn)
#  in the grid n×n
#  where 1≤xi≤n
#  and 1≤yi≤n
# .

# Let H
#  be the set of distinct Manhattan distances between any pair of cells. Your task is to maximize the size of H
# . Examples of sets and their construction are given in the notes.

# If there exists more than one solution, you are allowed to output any.

# Manhattan distance between cells (x1,y1)
#  and (x2,y2)
#  equals |x1−x2|+|y1−y2|
# .

# Input
# The first line contains a single integer t
#  (1≤t≤50
# ) — the number of test cases.

# Each of the following t
#  lines contains a single integer n
#  (2≤n≤103
# ).

# Output
# For each test case, output n
#  points which maximize the size of H
# . It is not necessary to output an empty line at the end of the answer for each test case.

# Example
# inputCopy
# 5
# 2
# 3
# 4
# 5
# 6
# outputCopy
# 1 1
# 1 2

# 2 1
# 2 3
# 3 1

# 1 1
# 1 3
# 4 3
# 4 4

# 1 1
# 1 3
# 1 4
# 2 1
# 5 5

# 1 4
# 1 5
# 1 6
# 5 2
# 5 5
# 6 1
# Note
# In the first testcase we have n=2
# . One of the possible arrangements is:

# The arrangement with cells located in (1,1)
#  and (1,2)
# .
# In this case H={|1−1|+|1−1|,|1−1|+|2−2|,|1−1|+|1−2|}={0,0,1}={0,1}
# . Hence, the size of H
#  is 2
# . It can be shown that it is the greatest possible answer.
# In the second testcase we have n=3
# . The optimal arrangement is:

# The arrangement with cells located in (2,1)
# , (2,3)
#  and (3,1)
# .
# H
# ={|2−2|+|1−1|,|2−2|+|3−3|,|3−3|+|1−1|,|2−2|+|1−3|,|2−3|+|1−1|,|2−3|+|3−1|}
# ={0,0,0,2,1,3}
# ={0,1,2,3}
# .

# For n=4
#  a possible arrangement is:


# For n=5
#  a possible arrangement is:


# For n=6
#  a possible arrangement is:





# Solution:
# The maximum number of distinct Manhattan distances is n
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n//2):
        print(1, i+1)
    for i in range(n//2, n):
        print(n, i+1)
