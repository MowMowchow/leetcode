#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    N = len(candidates)
    ans = []
    def rec(val, spot, arr):
      if val == target:
        return 1
      elif spot == N:
        return 0

      tval = val
      tarr = list(arr)
      while tval <= target:
        if rec(tval, spot+1, tarr):
          ans.append(tarr[:len(tarr)])
        tval += candidates[spot]
        tarr.append(candidates[spot])
      
      return 0
    
    rec(0, 0, [])
    
    return ans 
    
# @lc code=end

