#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # next node is 2^(level-1) indexes away
    # left = [2^(level): 2^(level)+1] <- from parent
    # right = [2^(level)+1: 2^(level)+2] <- from parent
    # have a base case for 0
    # need to know if current node is left or right to choose recurse
    def dfs(self, curr, depth, root, length, targetSum):
        if length == targetSum:
            return True
        else:
            left = (dfs(curr+2**(depth)))

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        

        
# @lc code=end

