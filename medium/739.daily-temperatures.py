#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    N = len(temperatures)
    stk = []
    ans = [0 for x in range(N)]
    
    for i in range(N-1, -1, -1):
      if not stk:
        stk.append(i)
      else:
        if temperatures[i] < temperatures[stk[-1]]:
          ans[i] = stk[-1]-i
        while stk:
          if temperatures[i] >= temperatures[stk[-1]]:
            stk.pop()
          else:
            ans[i] = stk[-1]-i
            break
        
        stk.append(i)
        
    return ans

# @lc code=end

