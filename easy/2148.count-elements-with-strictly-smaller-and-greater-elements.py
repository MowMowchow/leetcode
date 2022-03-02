class Solution:
  def countElements(self, nums: List[int]) -> int:
    N = len(nums)
    vis = {}
    ans = 0
    nums.sort()
    low = float("inf")
    high = -float("inf")
    for i in range(N):
      if nums[i] not in vis:
        vis[nums[i]] = 1
      else:
        vis[nums[i]] += 1
      low = min(low, nums[i])
      high = max(high, nums[i])
    
    for key in vis:
      if key != low and key != high:
        ans += vis[key]
        
    return ans
        