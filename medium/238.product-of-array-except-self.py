#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		out = [1 for x in range(len(nums))]
		temp = [1 for x in range(len(nums))]
		
		for i in range(1, n):
			out[i] *= out[i-1]
			out[i] *= nums[i-1]

		for i in range(n-2, -1, -1):
			temp[i] *= temp[i+1]
			temp[i] *= nums[i+1]
			out[i] *= temp[i]
		
		return out


# @lc code=end

