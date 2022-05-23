class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    tN = len(times)
    adj = [[] for x in range(n+1)]
    for u, v, w in times:
      adj[u].append([v, w])
    
    dist = [float("inf") for x in range(n+1)]
    q = [k]
    dist[k] = 0
        
    while q:
      curr = q.pop(0)
      for node, weight in adj[curr]:
        if dist[curr]+weight < dist[node]:
          dist[node] = dist[curr]+weight
          q.append(int(node))
    
    good = True
    high = -float("inf")
    for node in dist[1:]:
      high = max(high, node)
      if node == float("inf"):
        good = False
        
    return -1 if not good else high
      