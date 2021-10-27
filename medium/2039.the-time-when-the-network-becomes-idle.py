class Solution:
  def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
    # get dist from each node to root
    N = len(patience)
    adj = [[] for x in range(N+1)]
    for x, y in edges:
      adj[x].append(y)
      adj[y].append(x)
    
    dist = [float("inf") for x in range(N+1)]
    vis = [False for x in range(N+1)]
    dist[0] = 0
    
    q = [0]
    
    while q:
      curr = q.pop(0)
      if not vis[curr]:
        vis[curr] = True
        for node in adj[curr]:
          q.append(node)
          dist[node] = min(dist[node], dist[curr]+1)
    
    
    ans = 0
    # p = 1 -> dist*2 * 2
    # p < dist*2 -> dist*2 + (patience)
    # p > dist*2 -> dist*2
    
    for i in range(1, N):
      if patience[i] == 1:
        ans = max(ans, dist[i]*4)
      elif patience[i] <= dist[i]*2:
        ans = max(ans, (dist[i]*2-1)//patience[i] * patience[i] + dist[i]*2 + 1)
      else:
        ans = max(ans, dist[i]*2 + 1)
        
    return ans
    
    
    