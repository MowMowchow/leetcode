class Solution:
  def rearrangeArray(self, nums: List[int]) -> List[int]:
    negs = []
    pos = []
    N = len(nums)
    for i in nums:
      if i < 0:
        negs.append(i)
      else:
        pos.append(i)
    
    ans = []
    for i in range(len(pos)):
      ans.append(pos[i])
      ans.append(negs[i])
    
    return ans