class Solution:
  def countEven(self, num: int) -> int:
    ans = 0
    
    for i in range(1, num+1):
      sI = str(i)
      arr = [int(x) for x in sI]
      temp = sum(arr)
      if temp % 2 == 0:
        ans += 1
    
    return ans