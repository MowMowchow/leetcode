#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
class Solution:
  def calc(self, nums, divisor):
    total = 0
    for i in nums:
      if i % divisor == 0:
        total += i//divisor
      else:
        total += i//divisor+1
    return total
  
  def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    
    l = 1
    r = 1000000
    
    while l < r:
      mid = l + (r-l)//2
      res = self.calc(nums, mid)
      if res > threshold:
        l = mid+1
      else:
        r = mid
        
    return l
    
# @lc code=end

