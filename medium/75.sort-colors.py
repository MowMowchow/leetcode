#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    N = len(nums)
    cnt = [0, 0, 0]
    for i in range(N):
      cnt[nums[i]] += 1
    
    for i in range(N):
      nums[i] = 0 if i+1 <= cnt[0] else (1 if cnt[0] < i+1 <= cnt[0]+cnt[1] else 2)

    return nums
        
# @lc code=end

