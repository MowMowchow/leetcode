class Solution:
  def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
    N = len(values)
    adj = [[] for x in range(N)]
    ans = 0

    for a, b, c in edges:
      adj[a].append([b, c])
      adj[b].append([a, c])

    
    # print("!!!!!!!\n")
    def dfs(curr, currTime, currVal, vis):
      nonlocal ans
      
      if currTime <= maxTime:
        if curr == 0:
          # print("path:", vis, "| currTime:", currTime, "| currVal:", currVal)
          ans = max(ans, currVal)

        for node, weight in adj[curr]:
          if currTime+weight <= maxTime:
            if vis[node] == 0:
              newVis = list(vis)
              newVis[node] = 1
              dfs(node, currTime+weight, currVal+values[node], newVis)
            elif vis[node]:
              dfs(node, currTime+weight, currVal, vis)

    temp = [0 for x in range(N)]
    temp[0] = 1
    dfs(0, 0, values[0], temp)

    return ans