"""
We can solve this by running BFS on the cells with a rotten fruit. 
Pop the rotten cell into the queue. Then traverse the neighboring cells, ignoring cells that are out of bounds and cells that have already been visited (stored in a cache). Also, if the neighboring cell is a 0, ignore it. 
Push new neigboring cells into the queue that are equal to 1, which means that the fruit will become rotten. 

After popping all cells off the queue at the desired level, increment the answer. 
When the queue is empty, that means that all fruits have rotted. Return the answer. 

Edge case: no fresh fruits can become rotten. In this case, the logic above would return 1 instead of -1.
So, if the return value from BFS is 1, we return -1 for that group
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cache = set()
        def checkFreshFruits():
            for i in range(0, len(grid)):
                for j in range(0, len(grid[0])):
                    if grid[i][j] == 1:
                        return True
            
            return False

        def bfs(coords):
            q = deque()
            for coord in coords:
                q.append(coord)
            length = 0
            while len(q) > 0:
                for i in range(len(q)):
                    r, c = q.popleft()
                    cache.add((r, c))

                    neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                    for neighbor in neighbors:
                        dr = neighbor[0]
                        dc = neighbor[1]
                        if min((dr+r), (dc+c)) < 0:
                            continue
                        if (dr+r) >= len(grid) or (dc+c) >= len(grid[0]):
                            continue
                        if grid[dr+r][dc+c] != 1:
                            continue
                        if ((dr+r, dc+c)) in cache:
                            continue
                        grid[dr+r][dc+c] = 2
                        q.append((dr+r, dc+c))
                length += 1
            return length
        
        rottens = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2 and ((i, j)) not in cache:
                    rottens.append((i, j))
        
        minutes = bfs(rottens)
        if checkFreshFruits():
            return -1
        else:
            if minutes == 0:
                return 0
            else:
                return minutes -1