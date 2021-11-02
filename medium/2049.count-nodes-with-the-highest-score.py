class Solution:
  def countHighestScoreNodes(self, parents: List[int]) -> int:
    N = len(parents)
    adj = [[] for x in range(N+1)]
    subSize = [0 for x in range(N+1)]
    
    for i in range(1, N):
      adj[parents[i]].append(i)
      
    totals = {}
    best = [0, 0]
    

    def dfs(curr, prev):
      subSize[curr] = 1
      for node in adj[curr]:
        if node != prev:
          dfs(node, curr)
          subSize[curr] += subSize[node]
      
    
    def dfs2(curr, prev):
      cnt = 1
      subCnt = subSize[curr]
      for node in adj[curr]:
        if node != prev:
          cnt *= subSize[node]
          dfs2(node, curr)
      
      cnt *= N-(N-1 if subCnt == N else subCnt)
    
      if cnt not in totals:
        totals[cnt] = 1
      else:
        totals[cnt] += 1

        
    dfs(0, -1)
    dfs2(0, -1)
      
    for val in totals:
      if val > best[0]:
        best[0] = val
        best[1] = totals[val]
    

    return best[1]