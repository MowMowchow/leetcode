#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    N = len(s)
    skip = {}
    oi = []
    ans = ""
    
    for i in range(N):
      if s[i] == "(":
        oi.append(i)
      elif s[i] == ")":
        if oi:
          oi.pop()
        else:
          skip[i] = 1
    
    while oi:
      skip[oi.pop()] = 1
      
    for i in range(N):
      if i not in skip:
        ans += s[i]
        
    return ans 
    
# @lc code=end

