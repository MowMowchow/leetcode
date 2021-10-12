#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    N = len(nums)
    if N == 1:
      return 1
    
    dp = [1 for x in range(N+1)]
    ans = 0
    
    for i in range(N):
      for j in range(i):
        if nums[i] > nums[j]:
          dp[i] = max(dp[i], dp[j]+1)
      
      ans = max(ans, dp[i])
    
    
    return ans          
              
# @lc code=end

