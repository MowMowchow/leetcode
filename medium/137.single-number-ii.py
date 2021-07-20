#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    N = len(nums)
    a = 0
    b = 0
    
    for i in range(N):
      a = (a^nums[i])&(~b)
      b = (b^nums[i])&(~a)    
      
    return a 
    
# @lc code=end

