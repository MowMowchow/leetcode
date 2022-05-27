class Solution:
  def numberOfSteps(self, num: int) -> int:
    cnt = 0
    def rec(curr):
      nonlocal cnt
      if curr == 0:
        return 
      if curr % 2 == 0:
        cnt += 1
        rec(curr//2)
      else:
        cnt += 1
        rec(curr-1)
        
    
    rec(num)
    return cnt