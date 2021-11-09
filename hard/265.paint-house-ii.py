class Solution:
  def minCostII(self, costs: List[List[int]]) -> int:
    # n*k^2 | -> doing n*k is just keeping track of 2 mins (and respective house for collision)
    N = len(costs)
    k = len(costs[0])
    
    ans = [[float("inf") for x in range(k)] for y in range(N)]
    ans[0] = [x for x in costs[0]]
    
    for i in range(1, N):
      for root in range(k):
        for j in range(1, k):
          ans[i][root] = min(ans[i][root], ans[i-1][root-j]+costs[i][root])

    return min(ans[N-1])