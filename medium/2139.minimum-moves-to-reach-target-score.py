class Solution:
  def minMoves(self, target: int, maxDoubles: int) -> int:
    ans = 0
    def rec(curr, dC):
      nonlocal ans
      nonlocal target
      nonlocal maxDoubles
      
      if target == 1 or dC >= maxDoubles:
        return
      elif target % 2 == 0 and dC < maxDoubles:
        ans += 1
        dC += 1
        target //= 2
        rec(target, dC)
      else:
        ans += 1
        target -= 1
        rec(target, dC)
    
    rec(target, 0)
    
    return ans + target-1