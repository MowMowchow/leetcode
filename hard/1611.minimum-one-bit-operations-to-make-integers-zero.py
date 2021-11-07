#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#

# @lc code=start
class Solution:
  def minimumOneBitOperations(self, n: int) -> int:
    ans = 0
    
    # if the ith bit is set, it takes 2^i - 1 operations to unset
    
    sBit = bin(n)[2:]
    sN = len(sBit)
    
    for i in range(sN):
      if sBit[sN-i-1] == "1":
        ans = 2**(i+1)-1 - ans
    
    return ans
# @lc code=end

