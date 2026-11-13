"""
By definition, an island is found when we find a 1, run dfs from that node as the starting point, continue moving up, left, right, down if we find a 1, stop searching when a '0' is found. Once the dfs search is over, we add a new island to the final result. Each time we visit a node, we must track it so that we don't wind up running dfs on a big island that we've already found. We need to go through the full grid at least once, and then run dfs once we've hit an island cell that hasn't already been visited. 
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        def dfs(r, c):
            if min(r, c) < 0:
                return
            if r >= len(grid) or c >= len(grid[0]):
                return
            if (r, c) in visited:
                return
            if grid[r][c] == "0":
                return
            visited.add((r, c))
            # We're at an island cell that we haven't hit before. We should traverse in each direction, expanding until we've marked every cell as visited that's connected to this island. 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if ((i, j)) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands