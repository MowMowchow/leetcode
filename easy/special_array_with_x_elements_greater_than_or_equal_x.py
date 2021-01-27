class Solution:
  def bs(self, target, arr):
    low = 0
    high = len(arr)-1
    
    while low < high:
      mid = low+(high-low)//2
      
      if arr[mid] < target:
        low = mid+1
      else:
        high = mid

    return low
    
    
  def specialArray(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    nn = max(nums)
    
    for i in range(0, nn+1):
      temp = self.bs(i, nums)
      if n-temp == i:
        return i
      
    return -1