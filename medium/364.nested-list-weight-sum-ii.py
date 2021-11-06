# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
  def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    N = len(nestedList)  
    regSum = 0
    reverseSum = 0
    maxDepth = 1
    
    
    def dfs(currList, currDepth):
      nonlocal regSum, reverseSum
      res = currDepth
      
      for item in currList:
        if item.isInteger():
          regSum += item.getInteger()
          reverseSum += item.getInteger()*currDepth
        else:
          res = max(res, dfs(item.getList(), currDepth+1))
          
      return res
    
    
    maxDepth = dfs(nestedList, 1)
        
    return (regSum*(maxDepth+1))-reverseSum
