"""
The shortest path can be computed by running a bfs algorithm, starting from the top left cell. There are 8 possible directions to move (4 for each edge and 4 for each corner). We must try all 8 options and use a queue to maintain graph leveling when traversing through. Return -1 if there's a dead end that's hit (coordinate out of bounds), if the node isn't equal to 0. Return the length, which is incremented after processing the len(queue) for each level, if coordinates of graph equal n-1, n-1 and the value is equal to 0. 
 """
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        l = 0
        foundSolution = False
        def bfs():
            length = 1
            while len(q) > 0:
                for i in range(0, len(q)):
                    r, c = q.popleft()
                    visited.add((r, c))
                    if r == len(grid) - 1 and c == len(grid[0]) - 1 and grid[r][c] == 0:
                        return length
                    
                    # Edge case, starting node equals 1
                    if grid[r][c] == 1:
                        break
                    
                    directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1],[1, -1], [-1, 1], [1, 1]]
                    for direction in directions:
                        dr = direction[0]
                        dc = direction[1]
                        if dr + r < 0 or dc + c < 0:
                            continue
                        
                        if dr + r >= len(grid) or dc + c >= len(grid[0]):
                            continue
                        
                        if grid[dr + r][dc + c] == 1:
                            continue
                        
                        if ((dr + r, dc + c)) in visited:
                            continue
                        
                        q.append((dr + r, dc + c))
                    
                length += 1
            
            return -1
        
        return bfs()

