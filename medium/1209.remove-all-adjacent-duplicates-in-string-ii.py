#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
  def removeDuplicates(self, s: str, k: int) -> str:
    stk = [0]
    i = 0
    while i < len(s):
      # print(s)
      if i == 0 or s[i] != s[i-1]:
        stk.append(1)
      
      elif s[i] == s[i-1]:
        stk[-1] += 1
        
      if stk[-1] == k:
        s = s[:i-k+1]+s[i+1:]
        stk.pop(-1)
        i -= k
                
      i += 1
    
    return s

# @lc code=end

