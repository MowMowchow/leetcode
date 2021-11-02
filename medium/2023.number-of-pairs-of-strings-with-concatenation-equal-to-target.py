class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
      N = len(nums)
      total = 0
      
      for i in range(N):
        for j in range(N):
          if i != j:
            if nums[i] + nums[j] == target:
              total += 1
      
      return total