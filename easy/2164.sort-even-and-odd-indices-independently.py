class Solution:
  def sortEvenOdd(self, nums: List[int]) -> List[int]:
    ans = []
    
    odd = []
    even = []
    N = len(nums)
    for i in range(N):
      if i % 2 == 0:
        even.append(nums[i])
      else:
        odd.append(nums[i])
        
    odd.sort(reverse=True)
    even.sort()
    
    oN = len(odd)
    eN = len(even)
    
    for i in range(oN):
      ans.append(even.pop(0))
      ans.append(odd.pop(0))
    
    if even:
      ans.append(even.pop())
    if odd:
      ans.append(odd.pop())

    return ans