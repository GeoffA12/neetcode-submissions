class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = []
        obstacle = 'X'

        for i in range(len(obstacleGrid)):
            row = []
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    row.append(obstacle)
                else:
                    row.append(obstacleGrid[i][j])
            row.append(obstacle)
            dp.append(row)
        
        extraRow = [obstacle for h in range(len(dp[0]))]
        dp.append(extraRow)

        for r in range(len(dp) - 2, -1, -1):
            for c in range(len(dp[0]) - 2, -1, -1):
                if dp[r][c] == obstacle:
                    continue
                obstacleDown = 1 if dp[r+1][c] == obstacle else 0
                obstacleRight = 1 if dp[r][c+1] == obstacle else 0
                obstacles = obstacleDown + obstacleRight

                if obstacles == 0:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
                elif obstacles == 1:
                    if obstacleDown:
                        dp[r][c] = dp[r][c+1]
                    else:
                        dp[r][c] = dp[r+1][c]
                else:
                    if (r == len(dp) - 2 and c == len(dp[0]) - 2):
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 0

        if dp[0][0] == obstacle:
            return 0
        else:
            return dp[0][0]