#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    N = len(nums)
    oneIn = False
    for i in range(N):
      if nums[i] == 1:
        oneIn = True
      if nums[i] <= 0 or nums[i] > N:
        nums[i] = "N"
    
    if N == 1:
      return 1 if nums[0] == "N" else nums[0]+1
    
    if not oneIn:
      return 1
    
    for i in range(N):
      if nums[i] != "N" and nums[i] != "Y":
        if nums[int(nums[i])-1] == "N":
          nums[int(nums[i])-1] = "Y"
        else:
          nums[int(nums[i])-1] = str(nums[int(nums[i])-1])

    
    for i in range(N+1):
      if i == N:
        return N+1
      if not isinstance(nums[i], str) or nums[i] == "N":
        return i+1
      
# @lc code=end

