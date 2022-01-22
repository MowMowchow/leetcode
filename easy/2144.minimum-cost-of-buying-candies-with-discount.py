class Solution:
  def minimumCost(self, cost: List[int]) -> int:
    ans = 0
    
    cost.sort()
    
    while cost:
      curr1 = cost.pop(-1)
      ans += curr1
      if cost:
        curr2 = cost.pop(-1)
        ans += curr2
        if cost:
          cost.pop(-1)
      else:
        break
    
    return ans
      