#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # swap the last occurence where nums[i] < nums[i+1]
    # if there is no such case return nums[::-1]

    N = len(nums)
    k = -1
    r = -1
    for i in range(N-2, -1, -1):
      if nums[i] < nums[i+1]:
        k = i
        break
        
    if k == -1:
      for i in range(N//2):
        nums[i] += nums[N-i-1]
        nums[N-i-1] = nums[i]-nums[N-i-1]
        nums[i] -= nums[N-i-1]
  
    else:
      q = k+1
      for i in range(k+1, N):
        if nums[k] < nums[i] <= nums[q]:
          q = i
      
      nums[k] += nums[q]
      nums[q] = nums[k]-nums[q]
      nums[k] -= nums[q]
      if N-k-1 >= 2:
        for i in range(k+1, k+1+(N-k)//2):
          if i < N-(i-k):
            nums[i] += nums[N-(i-k)]
            nums[N-(i-k)] = nums[i]-nums[N-(i-k)]
            nums[i] -= nums[N-(i-k)]

# @lc code=end

