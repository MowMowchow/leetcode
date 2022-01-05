#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    vis = [False for x in range(n+1)]
    trusts = [[] for x in range(n+1)]
    
    for a, b in trust:
      vis[a] = True
      trusts[b].append(a)

    for i in range(1, n+1):
      if not vis[i] and len(trusts[i]) == n-1:
        return i

    return -1
 
# @lc code=end

