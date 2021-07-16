class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final = nums[0]
        n = len(nums)
        
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            final = max(final, nums[i])
    
        return final    