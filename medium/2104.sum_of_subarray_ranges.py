class Solution:
  def subArrayRanges(self, nums: List[int]) -> int:
    N = len(nums)
    ans = 0
    
    for left in range(N):
      low = float("inf")
      high = -float("inf")
      for size in range(N):
        if left+size < N:
          low = min(low, nums[left+size])
          high = max(high, nums[left+size])
          ans += abs(high-low)
    
    return ans