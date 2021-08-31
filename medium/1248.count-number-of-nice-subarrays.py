#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    arr = [0]
    N = len(nums)
    ans = 0
    
    for i in range(N):
      if nums[i] & 1:
        arr.append(i+1)
    
    arr.append(N+1)
    
    if len(arr) >= k+2:
      for i in range(1, len(arr)-k):
        ans += (arr[i]-arr[i-1])*(arr[i+k]-arr[i+k-1])
      
    return ans
    
# @lc code=end

