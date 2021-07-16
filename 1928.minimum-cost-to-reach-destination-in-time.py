#
# @lc app=leetcode id=1928 lang=python3
#
# [1928] Minimum Cost to Reach Destination in Time
#

# @lc code=start
class Solution:
  def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
    N = len(passingFees)
    M = len(edges)
    adj = [[] for x in range(N+1)]
    dp = [float("inf") for x in range(N+1)] 
    
    for a, b, c in edges:
      a += 1
      b += 1
      adj[a].append([b, c])
      adj[b].append([a, c])


    q = [[passingFees[0], 1, 0]]
    
    while q:
      cost, curr, time = heapq.heappop(q)
      
      if curr == N and time <= maxTime:
        return cost

      for node, time2 in adj[curr]:
        if time+time2 <= maxTime:
          if dp[node] >  time+time2 or dp[node] == float("inf"):
            dp[node] = time+time2
            heapq.heappush(q, list([cost+passingFees[node-1], node, time+time2]))

    
    return -1      
# @lc code=end

