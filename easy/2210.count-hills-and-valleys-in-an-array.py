class Solution:
  def countHillValley(self, nums: List[int]) -> int:
    N = len(nums)
    ans = 0
    
    for i in range(1, N):
      if nums[i] > nums[i-1]:
        
      if nums[i] < nums[i-1]:
        ans += 1
    
    
    return max(0, ans-1)