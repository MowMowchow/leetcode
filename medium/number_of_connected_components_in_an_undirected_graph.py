class Solution:
    def find(self, node, subsets):
        if subsets[node][0] != node:
            subsets[node][0] = self.find(subsets[node][0], subsets)
        return subsets[node][0]
    
    def union(self, u, v, subsets):
        if subsets[u][1] < subsets[v][1]:
            subsets[v][0] = subsets[u][0]
        elif subsets[u][1] > subsets[v][1]:
            subsets[u][0] = subsets[v][0]
        else:
            subsets[u][1] += 1
            subsets[v][0] = subsets[u][0]
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        subsets = [[x, 0] for x in range(n+1)]
        for edge in edges:
            x = self.find(edge[0], subsets)
            y = self.find(edge[1], subsets)
            self.union(x, y, subsets)
        
        cnt = 0
        for i in range(n):
            if i == subsets[i][0]:
               cnt += 1 
            
        return cnt