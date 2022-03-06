class Solution:
  def minimalKSum(self, nums: List[int], k: int) -> int:
    ans = 0
    N = len(nums)+1
    nums.append(0)
    nums.sort()
    diffs = []
    for i in range(1, N):
      if nums[i]-nums[i-1] > 1:
        diffs.append([nums[i-1]+1, nums[i]-1])
        
        
    def sumN(n):
      sumS = (n*(n+1))//2
      return sumS
  
    for l, r in diffs:
      rSum = sumN(r)
      lSum = sumN(l-1)
      add = rSum-lSum
      addK = r-l+1
      if addK > k:
        r = l+k-1
        rSum = sumN(r)
        add = rSum-lSum
        addK = r-l+1
        
      ans += rSum-lSum
      k -= r-l+1

      if k == 0:
        break
          
    if k > 0:
      l = nums[-1]+1
      r = l+k-1
      rSum = sumN(r)
      lSum = sumN(l-1)
      add = rSum-lSum
      addK = r-l+1
      ans += rSum-lSum

    return ans