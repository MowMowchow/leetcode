class Solution:
  def getDescentPeriods(self, prices: List[int]) -> int:
    N = len(prices)
    if N == 1:
      return 1
    s = []
    ans = 0
    l = 0
    r = 0 
    while r < N:
      if prices[r]-prices[r+1] == 1:
        r += 1
      else:
        s.append(r-l+1)
        r += 1
        l = r
      if r >= N-1:
        s.append(r-l+1)
        break
    
    
    for num in s:
      for i in range(num):
        ans += num-i
    
    return ans