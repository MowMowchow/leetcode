#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    N = len(nums)
    a = 0
    b = 0
    for i in range(N):
      a ^= nums[i]
    
    a &= -a
    
    for i in range(N):
      if a & nums[i]:
        b ^= nums[i]
    
    a = 0
    
    for i in range(N):
      a ^= nums[i]
      
    a ^= b
    
    return [a, b]   
    
# @lc code=end

