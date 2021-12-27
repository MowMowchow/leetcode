class Solution:
  def countPoints(self, rings: str) -> int:
    N = len(rings)
    ans = 0
    rods = [[] for x in range(10)]
    
    for i in range(0, N, 2):
      rods[int(rings[i+1])].append(rings[i])
          
    for rod in range(10):
      if 'R' in rods[rod] and 'G' in rods[rod] and 'B' in rods[rod]:
        ans += 1
    
    return ans