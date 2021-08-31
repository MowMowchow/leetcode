#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
  def integerBreak(self, n: int) -> int:
    # if remainder is 1 then take out last 3
    # otherwise just add a two
    if n == 2:
      return 1
    if n == 3:
      return 2
    threes = n//3
    twos = 0
    if not n % 3:
      pass
    elif (n % 3 == 2):
      twos += 1
    else:
      twos += 2
      threes -=1
    return (3**(threes))*(2**(twos)) 
    
# @lc code=end

