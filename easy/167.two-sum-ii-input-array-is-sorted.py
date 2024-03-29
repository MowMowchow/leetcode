#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    N = len(numbers)
    l = 0
    r = N-1;

    while l < r:
      if numbers[l] + numbers[r] > target:
        r -= 1
      elif numbers[l] + numbers[r] < target:
        l += 1
      else:
        return [l+1, r+1]

# @lc code=end

