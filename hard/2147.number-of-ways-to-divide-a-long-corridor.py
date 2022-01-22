class Solution:
  def numberOfWays(self, corridor: str) -> int:
    N = len(corridor)
    mod = 10**9 + 7
    corridor = [(0 if corridor[x] == "P" else 1) for x in range(N)]
    cSum = sum(corridor)
    ans = 1
    pc = -1
    cc = 0
    i = 0
    
    while i < N:
      if corridor[i]:
        cc += 1
        if cc == 3:
          ans *= int((pc if pc != -1 else 0)+1)%mod
          ans %= mod
          pc = 0
          cc = 1
      else:
        if cc == 2:
          if pc == -1:
            pc = 0
          pc += 1
      i += 1
    
    if (cSum % 2 == 1 or pc == -1) and not (len(corridor) == 2 and cSum == 2):
      return 0
      
    return ans  