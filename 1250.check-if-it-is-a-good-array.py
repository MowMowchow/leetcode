#
# @lc app=leetcode id=1250 lang=python3
#
# [1250] Check If It Is a Good Array
#

# @lc code=start
class Solution:
  def isGoodArray(self, nums: List[int]) -> bool:
    def gcd(a, b):
      return gcd(b, a%b) if b else a
    
    temp = nums[0]
    for i in nums[1:]:
      temp = gcd(temp, i)
    
    return True if temp == 1 else False
    
# @lc code=end

