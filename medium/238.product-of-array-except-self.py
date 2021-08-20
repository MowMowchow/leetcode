#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    N = len(nums)
    answer = [x for x in nums]
    
    for i in range(N-2, 0, -1):
      answer[i] *= answer[i+1]
    
    for i in range(1, N):
      nums[i] *= nums[i-1]
    
    answer[0] = answer[1]

    for i in range(1, N-1):
      answer[i] = answer[i+1]*nums[i-1]
      
    answer[N-1] = nums[N-2]
    
    return answer
        
# @lc code=end

