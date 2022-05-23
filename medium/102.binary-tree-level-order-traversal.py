# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    
    def dfs(curr, level):
      if curr:
        if len(ans) < level:
          ans.append([])
        ans[level-1].append(curr.val)

        if curr.left:
          dfs(curr.left, level+1)

        if curr.right:
          dfs(curr.right, level+1)
        
    
    dfs(root, 1)
    
    return ans
      