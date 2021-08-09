#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		N = len(coins)
		dp = [float("inf") for x in range(amount+1)]
		dp[0] = 0

		for w in range(1, amount+1):
			for i in range(N):
				if coins[i] <= w:
					dp[w] = min(dp[w-coins[i]]+1, dp[w])

		return dp[amount] if dp[amount] != float("inf") else -1

        
# @lc code=end

