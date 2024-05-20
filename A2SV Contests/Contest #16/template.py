
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

import sys, threading


def main():
    # your code
    
if name == 'main':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         memo = {}
        
#         def dp(idx, sell):
#             if idx >= len(prices):
#                 return 0
            
#             if (idx, sell) in memo:
#                 return memo[(idx, sell)]
            
#             if sell:
#                 mx = max(prices[idx] - fee + dp(idx + 1, False), dp(idx + 1, True))
#             else:
#                 mx = max(-prices[idx] + dp(idx + 1, True), dp(idx + 1, False))
            
#             memo[(idx, sell)] = mx
#             return mx
        
#         return dp(0, False)


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0
#         for coin in coins:
#             for i in range(coin , amount + 1):
#                 dp[i] = min(dp[i] , dp[i - coin] + 1)
#         # print(dp)
#         return -1 if dp[amount] == float('inf') else   dp[amount]


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         ans = [nums[0], nums[1]]

#         for i in range(2,len(nums)):
#             ans.append(nums[i] + max(ans[:i-1]))
#         # print(ans)
#         return max(ans)


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         memo = {}
        
#         def backtrack(i, sm):
#             if i == len(nums):
#                 return 1 if sm == target else 0
            
#             if (i, sm) in memo:
#                 return memo[(i, sm)]
            
#             memo[(i, sm)] = backtrack(i + 1, sm + nums[i]) + backtrack(i + 1, sm - nums[i])
            
#             return memo[(i, sm)]
        
#         return backtrack(0, 0)

