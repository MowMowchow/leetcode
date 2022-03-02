class Solution:
  def minimumSum(self, num: int) -> int:
    numS = str(num)    
    numL = [int(x) for x in numS]
    numL.sort()
    return int(str(numL[0])+str(numL[2])) + int(str(numL[1])+str(numL[3]))