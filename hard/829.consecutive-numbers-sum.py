#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start
class Solution:
  def consecutiveNumbersSum(self, n: int) -> int:
    ans = 0
    nr = int(sqrt(n))
    
    for k in range(1, 2*nr+1):
      temp = n/k - (k+1)/2
      
      if temp == int(temp) and temp >= 0:
        ans += 1
        
    return max(ans, 1)  

# @lc code=end

