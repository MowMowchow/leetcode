class Solution:
  def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    N = len(nums)
    before = []
    middle = []
    after = []
    
    for i in nums:
      if i < pivot:
        before.append(i)
      elif i > pivot:
        after.append(i)
      else:
        middle.append(i)
    
    ans = []
    for i in middle:
      before.append(i)
    for i in after:
      before.append(i)
    return before