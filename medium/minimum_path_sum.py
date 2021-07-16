class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        q = [[0, 0]]
        moves = [[1, 0], [0, 1]]
        visited = [[float("inf") for x in range(len(grid[0]))] for y in range(len(grid))]
        visited[0][0] = grid[0][0]
        # coloumn x row
        
        while q:
            cx, cy = q.pop(0)
            
            for mx, my in moves:
                if cx+mx < n and cy+my < m:
                    if visited[cy+my][cx+mx] > visited[cy][cx] + grid[cy+my][cx+mx]:
                        visited[cy+my][cx+mx] = visited[cy][cx] + grid[cy+my][cx+mx]
                        new = list([cx+mx, cy+my])
                        q.append(new)
                        if cx+mx == n-1 and cy+my == m-1:
                            break
            
        return visited[m-1][n-1]