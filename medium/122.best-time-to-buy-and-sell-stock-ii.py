class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    N = len(prices)
    
    prev = prices[0]
    ans = 0
    
    for i in prices:
      if i > prev:
        ans += i-prev
        prev = i
      else:
        prev = i
    
    return ans