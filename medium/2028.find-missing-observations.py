class Solution:
  def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # average = (average * nValues - value) / (nValues - 1)
        
    m = len(rolls)
    ans = []
    mean *= (n+m)

    for i in range(m):
      mean -= rolls[i]
      
    
    # print(mean)
    if mean / n < 1 or mean/n > 6 or mean <= 0:
      return []
    
    staticMean = int(mean)
    k = 0
    while k != n:
      ans.append(int(staticMean//n))
      mean -= int(staticMean//n)
      k += 1
    
    k = 0
    # print(mean)
    while mean != 0:
      if ans[k] == 6:
        k += 1
      else:
        ans[k] += 1
        mean -= 1
    
    

    return ans if len(ans) == n else []