#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
      n = (int(str(x)[::-1])) if x >= 0 else -(int(str(x*-1)[::-1]))
      return n if (-2)**31 <= n <= ((2)**31)-1 else 0
        
# @lc code=end

