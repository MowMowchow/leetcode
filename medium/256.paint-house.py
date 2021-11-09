class Solution:
  def minCost(self, costs: List[List[int]]) -> int:
    N = len(costs)
    ans = [[0 for x in range(3)] for y in range(2)]
    ans[0] = [x for x in costs[0]]
    
    
    for i in range(1, N):
      for j in range(3):
        ans[1][j] = min(ans[0][j-1], ans[0][j-2]) + costs[i][j]
      
      temp = list(ans[1])
      ans[0] = temp

    return min(ans[1 if N > 1 else 0])
      