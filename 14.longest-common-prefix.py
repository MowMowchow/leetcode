#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    final = ""
    for i in range(len(strs[0])):
      good = True
      for word in strs[1:]:
        if word[:i+1] != strs[0][:i+1]:
          good = False
          break

      if not good:
        break
      else:
        final = strs[0][:i+1]
        
    return final     
    
# @lc code=end

