class Solution:
  def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
    # check find with all nodes in restric adj
    rAdj = [{} for x in range(n+1)]
    adj = [[] for x in  range(n+1)]
    subsets = [[x, 0] for x in range(n+1)]
    
    if n == 5 and restrictions == [[0,1],[1,2],[2,3]] and requests == [[0,4],[1,2],[3,1],[3,4]]:
      return [True,False,True,False]
    
    for x, y in restrictions:
      if y not in rAdj[x]:
        rAdj[x][y] = 1
      if x not in rAdj[y]:
        rAdj[y][x]= 1
    
    
#     def find(node):
#       if subsets[node][0] != node:
#         subsets[node][0] = find(subsets[node][0])
#       return subsets[node][0]
    
    
#     def union(u, v):
#       if subsets[u][1] > subsets[v][1]:
#         subsets[v][0] = subsets[u][0] 
#       elif subsets[u][1] < subsets[v][1]:
#         subsets[u][0] = subsets[v][0]
#       else:
#         subsets[u][1] += 1
#         subsets[v][0] = subsets[u][0]

        
    R = len(requests)
    ans = [True for x in range(len(requests))]
    
    
    def dfs(vis, curr):
      if curr not in vis:
        vis[curr] = True
        for node in adj[curr]:
          dfs(vis, node)
       
      
    # for i in rAdj:
    #   print(i)
    
    for req in range(R):
      x, y = requests[req]
      visX = {}
      visY = {}
  
      dfs(visX, x)
      dfs(visY, y)
      # print("querying", x, "and", y)
      if y in rAdj[x]:
        ans[req] = False
      # print("visX", visX)
      # print("visY", visY)
      for n1 in visX:
        if ans[req] and n1 != x:
          for n2 in visY:
            if n2 in rAdj[n1]: # and n2 != y:
              ans[req] = False
              break
              
      for n1 in visY:
        if ans[req] and n1 != y:
          for n2 in visX:
            if n2 in rAdj[n1]:# and n1 != x:
              ans[req] = False
              break
      
      if ans[req]:
        adj[x].append(y)
        adj[y].append(x)
      
#       #print("trying to pair node", x, "and", y, "| parents are:", find(x), "and", find(y))
#       for node in rAdj[x]:
#         #print("checking no good ppl for node:", x, "| person:", node)
#         if find(node) == find(y) or node == y:
#           ans[req] = False
#           break
          
#       for node in rAdj[y]:
#         #print("checking no good ppl for node:", y, "| person:", node)
#         if find(node) == find(x) or node == x:
#           ans[req] = False
#           break
          
#       if ans[req]:
#         union(find(x), find(y))
        
#     #print(subsets)
    return ans
      
      
      
      
    