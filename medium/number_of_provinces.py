
class Solution:
    
  def dfs(self, curr, visited, adj, N):
    if not visited[curr]:
      visited[curr] = True
        
      for node in range(N):
        if adj[curr][node]:
          self.dfs(node, visited, adj, N)
        
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    N = len(isConnected)
    visited = [False for x in range(N+1)]
    cnt = 0
    for i in range(N):
        if not visited[i]:
          self.dfs(i, visited, isConnected, N)
            cnt += 1
              
    return cnt