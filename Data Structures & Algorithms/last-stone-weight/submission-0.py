import heapq

"""
1. Create a max heap from the input stones
[-2, -3, -6, -2, -4]
2. While the size of the heap is greater than 1, 
3. Get the largest 2 values in the heap, using nsmallest() (due to max heap negation)
4. Compare the values
5. If equal, pop off the heap twice
6. If one is bigger, store the difference and push the difference into the max heap
7. Continue
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            largest = -heapq.nsmallest(1, heap)[0]
            print(largest)
            second_largest = -heapq.nsmallest(2, heap)[1]
            print(second_largest)
            if largest == second_largest:
                heapq.heappop(heap)
                heapq.heappop(heap)
            else:
                heapq.heappop(heap)
                heapq.heappop(heap)
                difference = largest - second_largest
                heapq.heappush(heap, -difference)

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]


