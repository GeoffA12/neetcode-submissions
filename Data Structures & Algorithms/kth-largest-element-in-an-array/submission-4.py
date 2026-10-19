import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # largest = heapq.nlargest(k, nums)
        # return largest[len(largest) - 1]
        heap = []
        for num in nums:
            # If the element is smaller than the min value of the minHeap, push the element onto the heap.
            # If the element is size of the heap grows larger than k, then pop the heap. 
            # The largest value should be the bottom of the heap
            if len(heap) == 0:
                heapq.heappush(heap, num)
                continue
            
            if num > heap[0] or len(heap) < k:
                heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        if len(heap) == 1:
            return heapq.nsmallest(1, heap)[0]
        else:
            return heapq.nsmallest(len(heap) - 1, heap)[0]


        
