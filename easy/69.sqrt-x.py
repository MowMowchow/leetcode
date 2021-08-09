#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
  def bs(self, cap, target):
    l = 0
    r = cap
    ans = -1
    while (l <= r):
      mid = l+(r-l)//2
      if (mid*mid > target):
        r = mid-1
      else:
        ans = mid
        l = mid+1
    return ans
  
  def mySqrt(self, x: int) -> int:
    
    return self.bs(x, x)
        
# @lc code=end

