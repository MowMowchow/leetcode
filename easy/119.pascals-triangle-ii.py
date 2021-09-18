#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    ans = [0 for x in range(rowIndex+1)]
    ans[0] = 1
    
    for i in range(rowIndex+1):
      for j in range(i, 0, -1):
        ans[j] = ans[j]+ans[j-1]
        
    return ans
    
# @lc code=end

