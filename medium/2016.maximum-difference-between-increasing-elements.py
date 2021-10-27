class Solution:
  def maximumDifference(self, nums: List[int]) -> int:
    N = len(nums)
    low = 0
    ans = 0
    bad = True
    for i in range(1, N):
      if nums[i-1] < nums[i]:
        bad = False
        break
    if bad:
      return -1
    
    for i in range(1, N):
      if nums[i-1] < nums[low]:
        low = i-1
      ans = max(ans, nums[i]-nums[low])
      
    
    return ans
