# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
    q = []
    
    
    def dfs(target, curr):
      heappush(q, [abs(target-curr.val), curr.val])
      if curr.left:
        dfs(target, curr.left)
      if curr.right:
        dfs(target, curr.right)
    
    
    dfs(target, root)
    
    ans = []
    
    for i in range(k):
      ans.append(heappop(q)[1])
      
    
    return ans