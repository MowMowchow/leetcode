#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		adj = [[] for x in range(numCourses+1)]
		vis = [0 for x in range(numCourses+1)]
		out = [] 
		bad = False
		for a, b in prerequisites:
			adj[b].append(a)


		def dfs(curr, adj, vis, stack):
			nonlocal bad
			if bad:
				return False
			vis[curr] = 1
			res = True
			for node in adj[curr]:
				if vis[node] == 1:
					bad = True
					return False
				if vis[node] == 0:
					res = dfs(node, adj, vis, stack)

			vis[curr] = 2
			stack.append(curr)

			return res
		
		for i in range(numCourses):
			if bad:
				return []
			if vis[i] == 0:
				if not dfs(i, adj, vis, out):
					return []
		
		return out[::-1]


		
        
# @lc code=end

