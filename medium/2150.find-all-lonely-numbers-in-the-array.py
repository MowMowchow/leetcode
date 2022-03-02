class Solution:
  def findLonely(self, nums: List[int]) -> List[int]:
    vis = {}
    N = len(nums)
    for i in range(N):
      if nums[i] not in vis:
        vis[nums[i]] = 0
      vis[nums[i]] += 1
    
    ans = []
    for i in nums:
      if i+1 not in vis and not i-1 in vis and vis[i] == 1:
        ans.append(i)
    
    return ans