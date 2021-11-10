#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    N = len(tokens)
    ans = 0
    stk = []
    operators = {
      "+": 1,
      "-": 1,
      "*": 1,
      "/": 1
    }
    
    while tokens:
      top = tokens.pop(0)
      
      if top not in operators:
        stk.append(int(top))
      else:
        op2 = stk.pop()
        op1 = stk.pop()
        
        if top == "*":
          ans = op1*op2
        elif top == "/":
          ans = int(op1/op2)
        elif top == "+":
          ans = op1+op2
        elif top == "-":
          ans = op1-op2
        
        stk.append(ans)
    
    return stk.pop()
 
# @lc code=end

