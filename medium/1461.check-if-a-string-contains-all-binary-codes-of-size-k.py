class Solution:
  def hasAllCodes(self, s: str, k: int) -> bool:
    N = len(s)
    vis = {}
    if k > N:
      return 0
    
    r = k
    curr = [x for x in s[:r]]
    vis[tuple(curr)] = 1
    
    while r < N:
      curr.pop(0)
      curr.append(s[r])
      tupleCurr = tuple(curr)
      if tupleCurr not in vis:
        vis[tupleCurr] = 1
        
      r += 1
      
    return True if len(vis) == 2**k else False