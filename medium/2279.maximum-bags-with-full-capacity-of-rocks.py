class Solution:
  def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    diff = sorted([capacity[i]-rocks[i] for i in range(len(capacity))])
    ans = 0
    for i in range(len(diff)):
      if additionalRocks >= diff[i]:
        additionalRocks -= diff[i]
        ans += 1
      else:
        break
    
    return ans