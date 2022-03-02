class Solution:
  def smallestNumber(self, num: int) -> int:
    if num == 0:
      return 0
    if num < 0:
      num *= -1
      numS = str(num)
      numL = [int(x) for x in numS] 
      numL.sort(reverse=True)
      ans = "".join([str(x) for x in numL])
      return -1*int(ans)
    
    else:
      numS = str(num)
      numL = [int(x) for x in numS] 
      ans = ""
      numL.sort()
      lead = float("inf")
      if numL[0] == 0:
        for i in range(len(numL)):
          if numL[i] != 0:
            lead = numL.pop(i)
            break
        if lead != float("inf"):
          numL = [lead] + numL
        
      ans = "".join([str(x) for x in numL])
      return int(ans)