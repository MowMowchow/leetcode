# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return root
    
    
    l = root.left
    r = root.right
    
    root.left = None
    root.right = None
    
    while l:
      newL = l.left
      newR = l.right
      
      l.right = root 
      l.left = r
      root = l
      
      l = newL
      r = newR
      
      
    return root