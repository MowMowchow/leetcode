#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#

# @lc code=start
class Solution:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    Nr = len(routes)
    stopToRoute = {}
    
    for route in range(Nr):
      for stop in routes[route]:
        if stop not in stopToRoute:
          stopToRoute[stop] = {}
        stopToRoute[stop][route] = 1
    
    q = [[source, 0]]
    vis = {}
    visR = {}
    
    while q:
      curr, length = q.pop(0)
      
      if curr == target:
        return length
      elif curr not in vis:
        vis[curr] = 1
        for route in stopToRoute[curr]:
          if route not in visR:
            visR[route] = 1
            for stop in routes[route]:
              if stop not in vis:
                q.append(list([stop, length+1]))
            
    return -1
              
# @lc code=end

