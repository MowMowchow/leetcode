class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = [[] for x in range(numCourses)]
    vis = [False for x in range(numCourses)]
    recStk = [False for x in range(numCourses)]

    total = 0
    cyclic = False
    for a, b in prerequisites:
      adj[b].append(a)
    
    
    def dfs(curr):
      nonlocal total, cyclic
      if not vis[curr]:
        recStk[curr] = True
        vis[curr] = True
        total += 1
        for node in adj[curr]:
          dfs(node)
          if recStk[node]:
            cyclic = True
        
        recStk[curr] = False
        
    
    for course in range(numCourses):
      dfs(course)
    
    return total == numCourses and not cyclic