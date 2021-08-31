class Solution:
  def threeSumSmaller(self, nums: List[int], target: int) -> int:
    N = len(nums)
    total = 0
    nums.sort(reverse=True)
    print(nums)
    for i in range(N-1):
      l = i+1
      r = N-1
      
      while l < r:
        curr = nums[i] + nums[l] + nums[r]

        if curr < target:
          total += r-l
          r -= 1
        else:
          l += 1
          
    return total