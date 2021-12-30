#
# @lc app=leetcode id=1015 lang=python3
#
# [1015] Smallest Integer Divisible by K
#

# @lc code=start
class Solution:
  def smallestRepunitDivByK(self, k: int) -> int:
    vis = {}
    curr = 1
    cnt = 1
    while curr not in vis:
      vis[curr] = 1
      if not curr%k:
        return cnt
      else:
        curr = curr%k * 10%k
        curr %= k
        curr += 1
        curr %= k
        cnt += 1
        if curr == 0:
          return cnt
      
    return -1      

# @lc code=end

