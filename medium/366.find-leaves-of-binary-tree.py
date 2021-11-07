# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    depths = [[] for x in range(101)]
    
    def dfs(curr):
      if not curr.left and not curr.right:
        depths[0].append(curr.val)
        return 1

      res = -1
      if curr.left:
        res = dfs(curr.left)+1
      if curr.right:
        res = max(res, dfs(curr.right)+1)
      
      depths[res].append(curr.val)

      return res
    
    
    dfs(root)

    for item in depths:
      if item:
        ans.append(item)
        
    return ans