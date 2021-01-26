class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        grid = obstacleGrid
        # m = x & n = y
        grid = [[0 for x in range(m)] for x in range(n)]
        grid[0][0] = 1
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                grid[i][0] = 0
                break
            grid[i][0] = 1
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                grid[0][i] = 0
                break
            grid[0][i] = 1
            
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    grid[i][j] += grid[i-1][j] + grid[i][j-1]
                
            
            
        return grid[n-1][m-1]