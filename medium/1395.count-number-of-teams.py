#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

# @lc code=start
class Solution:
    def numTeams(self, rating: List[int]) -> int:
      N = len(rating)
      ans = 0
      dpa = [0 for x in range(N)]
      dpd = [0 for x in range(N)]

      for i in range(1, N):
        for j in range(i):
          if rating[i] > rating[j]:
            ans += dpa[j]
            dpa[i] += 1
          elif rating[i] < rating[j]:
            ans += dpd[j]
            dpd[i] += 1

      return ans
      
# @lc code=end

