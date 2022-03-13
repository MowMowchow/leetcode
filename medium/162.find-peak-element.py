class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    N = len(nums)
    l = 1
    r = N
    nums = [-float("inf")] + nums
    nums.append(-float("inf"))
    
    while l < r:
      mid = l+((r-l)//2)
      
      if nums[mid-1] < nums[mid] > nums[mid+1]:
        return mid-1
      elif nums[mid+1] >= nums[mid]: # increasing
        l = mid+1
      else:
        r = mid-1
    
    return l-1
        
        