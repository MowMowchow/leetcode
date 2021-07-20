#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    N = len(nums)
    
    left = list([x for x in nums])
    right = list([x for x in nums])
    final = []
    
    left[0] = nums[0]
    right[N-1] = nums[N-1]
    
    for i in range(1, N):
      if i % k != 0:
        left[i] = max(left[i-1], left[i])
    
    for i in range(N-2, -1, -1):
      if (i+1) % k != 0:
        right[i] = max(right[i+1], right[i])


    for i in range(N-k+1):
      final.append(max(right[i], left[i+k-1]))

    return final 
# @lc code=end

