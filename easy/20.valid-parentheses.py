#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
  def isValid(self, s: str) -> bool:
    N = len(s)
    stk = []
    
    for i in range(N):
      if s[i] == "(":
        stk.append(")")
        
      elif s[i] == "[":
        stk.append("]")
      
      elif s[i] == "{":
        stk.append("}")
      
      else:
        if stk:  # if the stack is not empty
          if stk[-1] != s[i]:  # mismatched brackets
            return False
          else:  # corect input
            stk.pop(-1)
        else:  # if the stack is empty, then the input is invalid (extra closing bracket)
          return False
    
    return True if not stk else False  # leftover brackets are invalid
    
# @lc code=end

