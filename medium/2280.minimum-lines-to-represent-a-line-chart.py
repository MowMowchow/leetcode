class Solution:
  def minimumLines(self, stockPrices: List[List[int]]) -> int:
    stockPrices.sort()
    def partOfLine(spot):
      x1, y1 = stockPrices[spot-1]
      x2, y2 = stockPrices[spot]
      x3, y3 = stockPrices[spot+1]
      m = (y3-y1)/(x3-x1)
      
      return (y1-(m*x1)) == (y2-(m*x2))
    
    if len(stockPrices) < 3:
      return 1 if len(stockPrices) == 2 else 0
    
    ans = 1
    for i in range(1, len(stockPrices)-1):
      if not partOfLine(i):
        ans += 1
    
    return ans
    