class Solution:
  def maximumInvitations(self, favorite: List[int]) -> int:
    N = len(favorite)
    par = [0 for x in range(N+1)]
    color = [0 for x in range(N+1)]
    mark = [0 for x in range(N+1)]
    adj = [[] for x in range(N+1)]
    indeg = [[] for x in range(N+1)]
    cycles = [[] for x in range(N+1)]
    edges = {}
    cyclenumber = 0
    seated = []
    
    for i in range(N):
      adj[i+1].append(favorite[i]+1)
      indeg[favorite[i]+1].append(i+1)
      edges[(i+1, favorite[i]+1)] = 1
    
    
    def dfs(u, p):
      nonlocal cyclenumber
      if color[u] == 2:
          return

      if color[u] == 1:
          cyclenumber += 1
          cur = p
          mark[cur] = cyclenumber
          while cur != u:
              cur = par[cur]
              mark[cur] = cyclenumber
          return

      par[u] = p
      color[u] = 1

      for v in adj[u]:
          if v == par[u]:
              continue
          dfs(v, u)

      color[u] = 2
      
    
    def dfs2(u, p):
      res = 1
      for node in indeg[u]:
        if (node == p):
          continue
        res = max(res, dfs2(node, p)+1)
        
      return res
    
    
    for i in range(N):
      if color[i] != 2:
        dfs(i, -1)
    

    for i in range(1, N+1):
      if mark[i] != 0:
        cycles[mark[i]].append(i)
        
    cycles.sort(key=lambda x: len(x))
    seated = list(cycles[-1])
    baseAns = len(seated)
    ans = 0
    
    for i in range(N):
      if (favorite[favorite[i]] == i):
        ans += dfs2(i+1, favorite[i]+1)
    
    
    return max(baseAns, ans)
        
  