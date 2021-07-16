class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = x & n = y
        grid = [[0 for x in range(m)] for x in range(n)]
        grid[0][0] = 1
        for i in range(n):
            grid[i][0] = 1
        for i in range(m):
            grid[0][i] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += grid[i-1][j] + grid[i][j-1]
                
        
        return grid[n-1][m-1]