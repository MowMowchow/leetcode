#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    N = len(nums)
    ans = []
    nums.sort(reverse=True)
    vis = {}
    
    for i in range(0, N-2):
      l = i+1
      r = N-1
      
      while l < r:
        if nums[i] + nums[l] + nums[r] == 0:
          temp = tuple([nums[i], nums[l], nums[r]])
          if temp not in vis:
            vis[temp] = 1
            ans.append([nums[i], nums[l], nums[r]])
          l += 1
          
        elif nums[i] + nums[l] + nums[r] < 0:
          r -= 1
        
        else:
          l += 1
      
    return ans    
     
# @lc code=end

