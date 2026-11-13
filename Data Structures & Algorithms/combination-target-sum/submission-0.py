class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        
        def backtrack(idx, remaining_target):
            if remaining_target == 0:
                res.append(stack.copy())
                return
            
            if remaining_target < 0:
                return
            
            for i in range(idx, len(nums)):
                stack.append(nums[i])
                backtrack(i, remaining_target - nums[i])
                stack.pop()
    
        backtrack(0, target)
        
        return res

        