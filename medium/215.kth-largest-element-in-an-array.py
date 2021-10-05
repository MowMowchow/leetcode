#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    N = len(nums)
    q = []
    for i in range(N):
      if len(q) == k:
        if q[0] < nums[i]:
          heappop(q)
          heappush(q, nums[i])
      else:
        heappush(q, nums[i])
    
    return q[0]    
    
# @lc code=end

