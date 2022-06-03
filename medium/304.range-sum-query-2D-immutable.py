class NumMatrix:
  arr = []
  R = 0
  C = 0

  def __init__(self, matrix: List[List[int]]):
    self.R = len(matrix)
    self.C = len(matrix[0])
    self.arr = [[0 for col in range(self.C+1)] for row in range(self.R+1)]
    for row in range(1, self.R+1):
      for col in range(1, self.C+1):
        self.arr[row][col] += self.arr[row-1][col] + self.arr[row][col-1] - self.arr[row-1][col-1] + matrix[row-1][col-1]

  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    return self.arr[row2+1][col2+1] - self.arr[row2+1][col1] - self.arr[row1][col2+1] + self.arr[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)