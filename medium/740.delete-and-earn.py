class Solution:
  def deleteAndEarn(self, nums: List[int]) -> int:
    N = len(nums) 
    freq = {}
    dp = [0 for x in range(10001)] 
    
    for num in nums:
      if num not in freq:
        freq[num] = 0
      freq[num] += num
      
    for i in range(1, 10001):
      tempAdd = 0
      if i in freq:
        tempAdd += freq[i]
      
      dp[i] = max(dp[i-1], tempAdd+dp[i-2])
    
    return dp[10000]