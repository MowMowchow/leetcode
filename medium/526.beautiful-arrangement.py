#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
  def countArrangement(self, n: int) -> int:
    ans = 0
    permsDone = {}
    
    def recurse(n, currLen, currVis):
      if currLen == n:
        return 1
      
      res = 0
      
      for i in range(1, n+1):
        if (i % (currLen+1) == 0 or (currLen+1) % i == 0) and i not in currVis:
          newVis = dict(currVis)
          newVis[i] = 1
          res += recurse(n, currLen+1, newVis)
      
      return res
  
    for i in range(1, n+1):
      tempVis = {}
      tempVis[i] = 1
      ans += recurse(n, 1, tempVis)
      
      
    return ans    
# @lc code=end

