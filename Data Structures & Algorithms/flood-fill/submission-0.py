"""
DFS algorithm. 
1. Set the starting point of the DFS search to the image[sr][sc] node in the matrix
2. Run DFS at that node. Create a hashset to keep track of visited nodes in the grid
3. Base cases
a) When neighboring node is not the same value as the source node, stop and return
b) When neighboring node is out of bounds on the grid, stop and return
c) When neighboring node is not equal to the original source, leave it alone and return. Don't continue searching on that path because it's a dead end
d) When neighboring node is equal to the original source node, swap the value with color. Continue searching in each neighboring direction. 
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source_value = image[sr][sc]
        visited = set()
        def dfs(r, c):
            if min(r, c) < 0:
                return
            if r >= len(image):
                return
            if c >= len(image[0]):
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            if image[r][c] != source_value:
                return
            if image[r][c] == source_value:
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image