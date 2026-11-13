"""
## Idea 1 (DP Solution bottom up approach)
* Same as above where you add two 0's to the end of the cost array. 
* Start at the end of the cost array. Compute dp[i] where dp[i] = cost[i] + min(dp[i-1], dp[i-2])
* Continue this for each index, until at the start of the dp array
* The answer is the min(dp[0], dp[1])
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[i] for i in range(0, len(cost))]

        dp.append(0)
        dp.append(0)

        ptr = len(cost) - 1

        while ptr >= 0:
            dp[ptr] = cost[ptr] + min(dp[ptr + 1], dp[ptr + 2])
            ptr -= 1
        
        return min(dp[0], dp[1])
        