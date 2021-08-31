#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    q = [[[0, 0, 0, 0], 0]]
    ans = [int(x) for x in target]
    
    vis = [[[[False for a in range(10)] for b in range(10)] for c in range(10)] for d in range(10)]
    
    for dead in deadends:
      vis[int(dead[0])][int(dead[1])][int(dead[2])][int(dead[3])] = True
    
    while q:
      cs, cm = q.pop(0)
      a, b, c, d = cs
      
      if not vis[a][b][c][d]:
        vis[a][b][c][d] = True
        
        if cs == ans:
          return cm
        

        for spot in range(4):
          temp1 = list(cs)
          temp2 = list(cs)
          temp1[spot] += 1
          temp1[spot] %= 10
          
          temp2[spot] -= 1
          temp2[spot] += 10
          temp2[spot] %= 10
          
          q.append(list([temp1, cm+1]))
          q.append(list([temp2, cm+1]))
    
    return -1   
    
# @lc code=end

