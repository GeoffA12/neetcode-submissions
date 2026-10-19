import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []
        def dfs(i):
            if i >= len(nums):
                res.append(sol.copy())
                return 
            
            # Add the number to the subarray
            sol.append(nums[i])
            dfs(i + 1)

            # Skip the number
            sol.pop()
            dfs(i + 1)
        
        dfs(0)

        return res



        