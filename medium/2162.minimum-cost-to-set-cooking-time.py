class Solution:
  def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
  
    def equiv(num, target):  # converting oven time to regular seconds
      numS = str(num)
      nS = len(numS)
      mins = 0
      secs = 0
      if nS == 4:
        mins = int(numS[:2])
        secs = int(numS[2:])
      elif nS == 3:
        mins = int(numS[0])
        secs = int(numS[1:])
      else:
        secs = int(numS)
      total = 0
      total += mins*60
      total += secs
      # print("equiv?", total, target, " | base:", num)
      return total == target
    
    def cost(startAt, num):
      numL = [int(x) for x in str(num)]
      total = 0
      # print("COSTING")
      # print(numL, startAt)
      if numL[0] != startAt:
        total += moveCost
        
      total += pushCost
      for i in range(1, len(numL)):
        if numL[i-1] != numL[i]:
          total += moveCost
        total += pushCost
        
        # print(total)
      # print("DONE")
      return total
    
    ans = float("inf")
    
    for i in range(1, 10000):
      if equiv(i, targetSeconds):
        ans = min(ans, cost(startAt, i))
        # print(i, "'s cost:", cost(startAt, i))
        
    
    # print("~~~~~")
    # print("960 cost:", cost(1, 960))
    
    return ans 