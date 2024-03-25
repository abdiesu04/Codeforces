""""
Now that the war has ended, Ethiopians are celebrating their heroic win with a soccer league. In the soccer league with n
 teams, each team plays exactly once against every other team, resulting in a total of n⋅(n−1)2
 matches. The point system follows standard soccer rules: a win earns 3 points, a loss earns 0 points, and a draw earns 1 point for both teams.

After all matches are played, a team is assigned an m
-th rank if exactly m−1
 teams have strictly higher points than that team. Specifically, a team is considered top-k
 if its rank is no more than k
 (1≤rank≤k)
. Note that two teams might have the same rank.

You are asked to determine the minimum points required for a team to secure a top-k
 position. In other words, find the minimum p
 such that a team with p
 points remains among the top-k
 teams regardless of all possible match outcomes.

Input
The input consists of multiple test cases. The first line contains an integer T
 (1≤T≤105)
, the number of test cases. Each of the following T
 lines describes a test case, consisting of two integers n
 and k
 (2≤n≤106,1≤k≤n)
.

Output
For each test case, print an integer representing the minimum points required for a team to secure a top-k
 position.

Example
inputCopy
3
2 1
2 2
10 5
outputCopy
1
0
19
Note
In the first 2 testcases, we have 2
 teams, so in total there is only one match in the league. Here are the three possible outcomes of the league.

Team1 wins:
Team	Point	Rank
Team1	3
1
Team2	0
2
Team2 wins:
Team	Point	Rank
Team2	3
1
Team1	0
2
Draw:
Team	Point	Rank
Team1	1
1
Team2	1
1
For testcase 1, we can see that in a 2
-team league, a team with 3
 or 1
 point guarantees being top-1
. Therefore, the minimum point to guarantee top-1
 is 1
.

For testcase 2, we can see that in a 2
-team league, a team with 3
, 1
, or 0
 points guarantees being top-2
. The minimum is 0
.
"""

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0:
        print(min(n - k, k - 1))
    else:
        print(min(n - k, k - 1, n // 2))