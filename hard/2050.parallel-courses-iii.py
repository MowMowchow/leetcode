class Solution:
  def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
    N = len(time)
    adj = [[] for x in range(N+1)]
    time = [0]+time
    largest = 0
    dp = [-1 for x in range(N+1)]
    
    for i in range(len(relations)):
      adj[relations[i][0]].append(relations[i][1])

      
    def dfs(curr, prev):
      if dp[curr] == -1:
        high = 0
        res = 0
        for node in adj[curr]:
          if node != prev:
            res = dfs(node, curr)
            high = max(high, res)
        
        dp[curr] = high+time[curr]
      return dp[curr]
    
    
    for i in range(1, N+1):
      if dp[i] == -1:
        largest = max(largest, dfs(i, -1))
    
    return largest