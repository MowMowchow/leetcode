class Solution:
  def findFinalValue(self, nums: List[int], original: int) -> int:
    vis = {}
    N = len(nums)
    for i in nums:
      if i not in vis:
        vis[i] = 0
      vis[i] += 1
      
    curr = original
    
    while vis and curr in vis:
      vis[curr] -= 1
      if vis[curr] == 0:
        del vis[curr]
      curr *= 2
    
    return curr