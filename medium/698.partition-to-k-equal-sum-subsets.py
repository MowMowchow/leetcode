#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    numsTotal = sum(nums)
    N = len(nums)
    if numsTotal % k == 0:
      target = numsTotal//k
    else:
      return False
    
    
    vis = [False for x in range(N)]
    cnt = 0
    
    
    def recurse(currInd, currSum, total):
      if total == k:
        return True
      elif currSum == target:
        return recurse(0, 0, total+1)
      elif currSum > target:
        return False
      else:
        for i in range(currInd, N):
          if not vis[i]:
            vis[i] = True
            
            if recurse(i, currSum+nums[i], total):
              return True
            
            vis[i] = False
      
      return False
    
    
    return recurse(0, 0, 0)  
  
# @lc code=end

