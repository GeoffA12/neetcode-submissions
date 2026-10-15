import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for i in range(0, len(nums)):
            heapq.heappush(self.heap, nums[i])
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == 0 or val >= heapq.nsmallest(1, self.heap)[0]:
            heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # return heapq.nsmallest(1, self.heap)[0]
        return self.heap[0]
        