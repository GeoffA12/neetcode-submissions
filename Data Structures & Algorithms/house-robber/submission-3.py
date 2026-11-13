class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[i] for i in range(len(nums))]

        for i in range(2, len(dp)):
            if i == 2:
                m = dp[i-2]
            else:
                m = max(dp[i-3], dp[i-2])
            val = nums[i] + m
            dp[i] = val
            
            
        return max(dp[len(nums) - 1], dp[len(nums) - 2])