"""
What we care about is tracking the number of cells that are within an island, once an island is found. 
We can do this by running dfs on a cell once we see that we've hit a land cell. Keep track of all visited nodes when searching through the island, moving in all 4 directions. Only traverse to the next cell if it's not outside the grid and it's a land cell. Need to keep track of the total number of islands found when running dfs. Return the result. 

Continue looping through the outer grid cells until we've measured all islands. Store the island area in a list where the values in the list are the areas returned from running dfs. Return max value in the list. 
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cache = set()
        def dfs(r, c, depth):
            cache.add((r, c))
        
            neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            for neighbor in neighbors:
                dr = neighbor[0]
                dc = neighbor[1]
                if min((dr + r), (dc + c)) < 0:
                    continue
                if (dr + r) >= len(grid) or (dc + c) >= len(grid[0]):
                    continue
                if ((dr + r, dc + c)) in cache:
                    continue
                if grid[dr + r][dc + c] == 0:
                    continue
                depth = dfs(dr + r, dc + c, depth + 1)
            return depth
    
        areas = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1 and ((i, j)) not in cache:
                    area = dfs(i, j, 1)
                    areas.append(area)
        
        if areas:
            return max(areas)
        else:
            return 0
        