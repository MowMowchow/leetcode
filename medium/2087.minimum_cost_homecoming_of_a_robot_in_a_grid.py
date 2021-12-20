class Solution:
  def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
    return (sum(rowCosts[startPos[0]+1:homePos[0]+1]) if homePos[0] > startPos[0] else sum(rowCosts[homePos[0]:startPos[0]]))+(sum(colCosts[startPos[1]+1:homePos[1]+1]) if homePos[1] > startPos[1] else sum(colCosts[homePos[1]:startPos[1]]))
