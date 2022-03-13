class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    sN = len(s)
    tN = len(t)
    dp = {}    
    
    def rec(si, ti):
      if ti == tN:
        return 1
      elif si >= sN or ti >= tN:
        return 0
      elif (si, ti) not in dp:
        dp[(si, ti)] = 0
        if s[si] == t[ti]:
          dp[(si, ti)] += rec(si+1, ti+1)
        dp[(si, ti)] += rec(si+1, ti)
        
      return dp[(si, ti)]
   
  
    rec(0, 0)
    return dp[(0, 0)]
