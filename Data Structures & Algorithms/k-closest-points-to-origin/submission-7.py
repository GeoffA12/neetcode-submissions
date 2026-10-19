import heapq
import math

class Solution:
    """
   " 1. Use a max heap to keep track of the points that have the highest distance from origin
    2. For each point in points
    3. Run the distance formula where x1 = 0 , x2 = point[x], y1 = 0, y2 = point[y]
    4. if dist[x2, y2] < distMap[heap[0]]:
    5. Push to heap
    6. if len(heap) > k:
    7. Pop from the heap (pop the max distance coordinate off the heap)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_heap = []
        point_heap = []
        x1 = 0
        y1 = 0

        for point in points:
            x2 = point[0]
            y2 = point[1]

            if len(dist_heap) == 0:
                dist = -self.distance(x1, x2, y1, y2)
                heapq.heappush(dist_heap, dist)
                store_value = x2 + y2
                heapq.heappush(point_heap, (dist, point))
                continue
            
            dist = self.distance(x1, x2, y1, y2)
            if dist <= -dist_heap[0] or len(dist_heap) < k:
                heapq.heappush(dist_heap, -dist)
                store_value = x2 + y2
                heapq.heappush(point_heap, (-dist, point))

                if len(dist_heap) > k:
                    heapq.heappop(dist_heap)
                if len(point_heap) > k:
                    heapq.heappop(point_heap)

        res = []
        for tup in point_heap:
            _, point = tup
            res.append(point)
        return res

    def distance(self, x1: int, x2: int, y1: int, y2: int):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        