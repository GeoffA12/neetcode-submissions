class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[i] for i in range(len(nums))]

        for i in range(0, len(dp) -  2):
            neighbor = i + 2
            while neighbor <= len(dp) - 1:
                if dp[i] + nums[neighbor] > dp[neighbor]:
                    dp[neighbor] = dp[i] + nums[neighbor]
                neighbor += 1
            print(dp)
            
        return max(dp[len(nums) - 1], dp[len(nums) - 2])



