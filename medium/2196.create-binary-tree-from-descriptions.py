# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    N = len(descriptions)
    
    adj = [[] for x in range(100001)]
    
    parent = [-1 for x in range(100001)]
    
    for par, child, isLeft in descriptions:
      adj[par].append([child, isLeft])
      parent[child] = par
    
    root = adj[descriptions[0][0]][0][0]
    while parent[root] != -1:
      root = parent[root]
      
    
    tree = TreeNode()
    
    def dfs(curr, prev, tCurr):
      tCurr.val = curr
      for node, isLeft in adj[curr]:
        if prev != node:
          if isLeft:
            tCurr.left = TreeNode()
            dfs(node, curr, tCurr.left)
          else:
            tCurr.right = TreeNode()
            dfs(node, curr, tCurr.right)
    
    
    dfs(root, -1, tree)
    
    return tree
      
      
      
      