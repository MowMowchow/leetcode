#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    N = len(nums)
    L = [0 for x in range(N)]
    R = [0 for x in range(N)]
    L[0] = nums[0]
    R[N-1] = nums[N-1]
    
    for i in range(1, N):
      L[i] = min(nums[i], L[i-1])
    
    for i in range(N-2, -1, -1):
      R[i] = max(nums[i], R[i+1])

    for i in range(1, N-1):
      if L[i-1] < nums[i] < R[i+1]:
        return True
    
    return False
    
# @lc code=end

