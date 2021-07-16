#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
  def bs(self, arr, n ,x):
    l = 0
    r = n-1
    while l < r:
      mid = l+(r-l+1)//2
      if arr[mid] > x:
        r = mid-1
      else:
        l = mid
    return l if l < n and arr[l] < l else l+1

  
  def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    envelopes.sort(key = lambda x: (x[0], -x[1]));
    final = 0
    N = len(envelopes)
    dp = [float("inf") for x in range(N+1)]
    dp[0] = -float("inf")

    for i in range(N):
      j = max(self.bs(dp, N, envelopes[i][1]), 1)
      if dp[j-1] < envelopes[i][1] < dp[j]:
        dp[j] = envelopes[i][1]
        final = max(final, j)

    return final



# @lc code=end

