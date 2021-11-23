class Solution:
  def maxDistance(self, colors: List[int]) -> int:
    N = len(colors)
    best = 0
    
    for i in range(N):
      for j in range(N):
        if i != j and colors[i] != colors[j]:
          best = max(best, i-j)
    
    return best