#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
  def findMin(self, nums: List[int]) -> int:
    N = len(nums)
    
    if N == 1:
      return nums[0]
    elif N == 2:
      return min(nums)
    
    l = 1
    r = N-2
    
    while l <= r:
      mid = l + (r-l)//2
      
      if nums[mid] < nums[mid-1]:
          return nums[mid]
      elif nums[mid] > nums[mid+1]:
          return nums[mid+1]
      
      else:
        if nums[mid] > nums[0]:
          l = mid+1
        else:
          r = mid-1
    
    return nums[0]
      
# @lc code=end

