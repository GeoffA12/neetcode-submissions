"""
Naive solution
* Run DFS on the grid. Keep track of visited nodes to prevent infinite loops
* go as far right as possible
* go as far down as possible
* go as far left as possible
* go as far up as possible
* Base case: hit a node where you cannot move left, right, up, or down without either hitting a visited node or going out of bounds on the matrix
* At each recursive call, we need to append to an array that keeps track of the node ID we're visiting, so that we can return the array in the order of nodes that we processed (should be a spiral)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()

        def dfs(r, c, direction, ans):
            if r >= len(matrix):
                return ans
            
            if c >= len(matrix[0]):
                return ans
            
            if min(r, c) < 0:
                return ans

            if ((r, c)) in visited:
                return ans
            
            ans.append(matrix[r][c])
            visited.add((r, c))
            # print(direction)
            if direction == 'right':
                if ((r, c + 1)) in visited or c + 1 >= len(matrix[0]):
                    # Dead end
                    if ((r + 1, c)) in visited:
                        return ans
                    else:
                        ans = dfs(r + 1, c, 'down', ans)
                else:
                    ans = dfs(r, c + 1, direction, ans)
                
            if direction == 'down':
                if ((r + 1, c)) in visited or r + 1 >= len(matrix):
                    if ((r, c - 1)) in visited:
                        return ans
                    else:
                        ans = dfs(r, c - 1, 'left', ans)
                else:
                    ans = dfs(r + 1, c, direction, ans)
            
            if direction == 'left':
                if ((r, c - 1)) in visited or c - 1 < 0:
                    if ((r - 1, c)) in visited:
                        return ans
                    else:
                        ans = dfs(r - 1, c, 'up', ans)
                else:
                    ans = dfs(r, c - 1, direction , ans)
                
            if direction == 'up':
                if ((r - 1, c)) in visited:
                    if ((r, c + 1)) in visited:
                        return ans
                    else:
                        ans = dfs(r, c + 1, 'right', ans)
                else:
                    ans = dfs(r - 1, c, direction, ans)

            return ans
        

        return dfs(0, 0, 'right', [])

        