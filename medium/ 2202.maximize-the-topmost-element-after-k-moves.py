class Solution:
  def maximumTop(self, nums: List[int], k: int) -> int:
    N = len(nums)
    ans = -1
    if N == 1 and k % 2 == 1:
      return -1
    
    if k == 0:
      return nums[0]
    
    for i in range(min(N, k-1)):
      ans = max(ans, nums[i])
    
    if N > k:
      ans = max(ans, nums[k])
    
    return ans 