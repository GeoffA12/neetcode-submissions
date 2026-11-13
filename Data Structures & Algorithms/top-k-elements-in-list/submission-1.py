"""
Naive solution
1. Store the most frequent numbers on a min heap
2. The top of the heap (min) would be the kth largest element in the list
3. Any number we encounter that is larger than the top of the heap would be added, then pop the min value off of the heap if and only if the size of the heap exceeds k
4. Pushing to the heap would automatically reshuffle so that the smallest element is at head
5. Each entry in the heap would contain the numeric value and frequency as a tuple
6. Keep a map that keeps track of new numbers that don't exist yet in the heap, and those that do exist in the heap. Numbers encountered that do exist in the heap need to be retrieved from the map, and the existing frequency needs to be compared against whatever the kth largest element is at the top of the heap
"""
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        numFrequencyDict = {}

        for i in range(0, len(nums)):
            if nums[i] not in numFrequencyDict:
                numFrequencyDict[nums[i]] = 1
            else:
                numFrequencyDict[nums[i]] += 1
            
        for key, value in numFrequencyDict.items():
            heapq.heappush(heap, (-value, key))
        
        # print(heap)

        res = []
        for i in range(0, k):
            tup = heapq.heappop(heap)
            val, key = tup
            res.append(key)
        
        return res
        