#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    def calc(x, y):
      return ((x**2)+(y**2))**.5
    
    
    N = len(points)
    arr = []
    
    for i in range(N):
      arr.append([calc(points[i][0], points[i][1]), i])
      
    arr.sort()
    
    return [points[arr[i][1]] for i in range(k)]
        
# @lc code=end

