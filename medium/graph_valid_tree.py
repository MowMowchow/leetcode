class Solution:
    def bfs(self, curr, visited, adj):
        q = [[curr, curr]]
        
        while q:
            curr, prev = q.pop(0)

            visited[curr] = True
            for node in adj[curr]:
                if not visited[node]:
                    q.append(list([node, curr]))
                elif visited[node] and node != prev:
                    return False
            
        return True
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        cnt = 0
        visited = [False for x in range(n+1)]
        adj = [[] for x in range(n+1)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        
        for i in range(n):
            if not visited[i]:
                cnt += 1
                if cnt > 1:
                    return False
                if not self.bfs(i, visited, adj):
                    return False
                
        return True
                
        