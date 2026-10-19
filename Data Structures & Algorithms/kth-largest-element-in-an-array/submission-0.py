import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        # [2, 3, 1, 5, 4] k = 2
        # [4, 5]
        largest = heapq.nlargest(k, nums)
        return largest[len(largest) - 1]

        
