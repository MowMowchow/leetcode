# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    root2 = TreeNode()
    ans = ""
    path = []
    def dfs(curr):
      nonlocal root2
      if not curr:
          return False

      left = dfs(curr.left)
      right = dfs(curr.right)

      mid = curr.val == startValue or curr.val == destValue

      if mid + left + right >= 2:
        root2 = curr

      return mid or left or right
    
    dfs(root)  
      
      
    def dfsPath(root, key):
      nonlocal path
      if root:
        if root.val == key:
          return True

        path += ['L']
        if(dfsPath(root.left, key)):
          return True

        path.pop()
        path += ['R']
        if(dfsPath(root.right, key)):
          return True

        path.pop()

        return False
      return False
      
      
    def dfsLen(curr, currLen, target):
      if not curr:
        return 0
      if curr.val == target:
        return currLen
      
      left = dfsLen(curr.left, currLen+1, target)
      right = dfsLen(curr.right, currLen+1, target)
      
      return max(left, right)
      
    if (root2.val != startValue and root2.val != destValue):
      first = dfsLen(root2, 0, startValue)
      second = dfsPath(root2, destValue)
      # print(first, second)
      ans += "U"*first
      ans += "".join(path)
    
    elif (root2.val == startValue):
      dfsPath(root2, destValue)
      ans += "".join(path)
    
    elif (root2.val == destValue):
      ans += dfsLen(root2, 0, startValue)*"U"
    
      
    
    return ans
