class Solution:
  def minimumMoves(self, s: str) -> int:
    N = len(s)
    zero = False
    ans = 0
    
    i = 0
    
    while i < N:
      if "X" == s[i]:
        ans += 1
        i += 3
      else:
        i += 1
    
    return ans