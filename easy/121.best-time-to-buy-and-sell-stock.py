#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      N = len(prices)
      low = 0
      final = 0

      for i in range(1, N):
        if prices[i]<prices[low]:
          low = i
        final = max(final, prices[i]-prices[low])

      return final
        
# @lc code=end

