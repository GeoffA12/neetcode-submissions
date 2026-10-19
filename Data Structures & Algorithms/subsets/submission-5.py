from collections import deque
import copy
"""
1. Track all combinations in a 2D array
2. Go through each number in nums. Each element in the array can be stored as a unique subset (individually)
3. For combinations, we need to keep track of whether or not we've seen the same combination of numbers (in any order)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        completed = [False for i in range(0, len(nums))]
        res = []
        res.append([])
        # for i in range(0, len(nums)):
        self.goRight(nums, 0, res)
        return res

    def goRight(self, nums, idx, res):
        cache = {tuple(solution) for solution in res}
        next = idx
        local_solutions = []
        while next < len(nums):
            for i in range(0, len(local_solutions)):
                sol = local_solutions[i]
                potential_solution = copy.deepcopy(sol)
                potential_solution.append(nums[next])
                tup = tuple(potential_solution)
                if tup not in cache:
                    res.append(potential_solution)
                    cache.add(tup)
                    local_solutions.append(potential_solution)
            
            if (nums[next],) not in cache:
                res.append([nums[next]])
                cache.add((nums[next],))
                local_solutions.append([nums[next]])
            
            if idx != next and (nums[idx], nums[next]) not in cache:
                res.append([nums[idx], nums[next]])
                cache.add((nums[idx], nums[next]))
                local_solutions.append([nums[idx], nums[next]])

            next += 1

