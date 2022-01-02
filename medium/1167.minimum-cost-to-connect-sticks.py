class Solution:
  def connectSticks(self, sticks: List[int]) -> int:
    ans = 0
    heapify(sticks)
    while len(sticks) > 1:
      a = heappop(sticks)
      b = heappop(sticks)
      ans += a + b
      heappush(sticks, a+b)
    
    return ans
      