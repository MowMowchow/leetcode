class Solution:
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    N = len(nums)
    maxN = max(nums)
    maxOR = 0
    arr = []
    vis = {}
    total = 0
    
    arr = [x for x in nums]
        
    
    for i in arr:
      maxOR = max(maxOR, i | maxN)
      
    N = len(arr)
    
    def rec(curr, val):
      # print(curr, val)
      nonlocal total
      nonlocal maxOR
      if val not in vis and curr == N:
        vis[val] = 1
        return
      elif val in vis and curr == N:
        vis[val] += 1
        return
      

      rec(curr+1, val | arr[curr])
      rec(curr+1, val)
        
    rec(0, 0)
    
    for i in vis:
      maxOR = max(maxOR, i)
    
    return vis[maxOR]
        