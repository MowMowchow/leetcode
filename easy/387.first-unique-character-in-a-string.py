#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
  def firstUniqChar(self, s: str) -> int:
    N = len(s)
    vis = [[0, -1] for x in range(  26)]
    
    for i in range(N):
      ind = ord(s[i])-ord('a')
      if not vis[ind][0]:
        vis[ind][1] = i
      vis[ind][0] += 1
      
    for i in range(N):
      ind = ord(s[i])-ord('a')
      if vis[ind][0] == 1:
        return vis[ind][1]
      
    return -1
    
# @lc code=end

