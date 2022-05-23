class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    N = len(nums)
    vis = {}
    ans = 0
    for num in nums:
      if num not in vis:
        vis[num] = 0

      vis[num] += 1
      
    
    for key in vis:
      while vis[key] > 0:
        if k-key in vis and key != k-key:
          if vis[k-key] > 0:
            vis[key] -= 1
            vis[k-key] -= 1
            ans += 1
          else:
            break
        elif k-key in vis and key == k-key:
          if vis[key] > 1:
            vis[key] -= 1
            vis[k-key] -= 1
            ans += 1
          else: 
            break
        else:
          break
    
    return ans
            
      
      
        