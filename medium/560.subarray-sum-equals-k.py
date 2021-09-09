#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    N = len(nums)
    mapp = {}
    ans = 0
    
    for i in range(1, N):
      nums[i] += nums[i-1]
    
    for i in range(N):
      if nums[i] == k:
        ans += 1
      if i > 0:
        if nums[i-1] not in mapp:
          mapp[nums[i-1]] = 1
        else:
          mapp[nums[i-1]] += 1
        if nums[i]-k in mapp:
          ans += mapp[nums[i]-k]
      
    return ans
        
# @lc code=end

