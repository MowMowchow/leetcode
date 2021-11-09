class Solution:
  def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
    N = len(nums)
    ins = N-1 if a > 0 else 0
    ans = [0 for x in range(N)]
    l = 0
    r = N-1
    
    
    def calc(x, a, b, c):
      return (a*(x**2)+b*x+c)
    
    
    while l <= r:
      lAmt = calc(nums[l], a, b, c)
      rAmt = calc(nums[r], a, b, c)
      
      if a > 0:
        ans[ins] = lAmt if lAmt > rAmt else rAmt
        ins -= 1
        if lAmt > rAmt:
          l += 1
        else:
          r -= 1
      else:
        ans[ins] = lAmt if lAmt < rAmt else rAmt
        ins += 1
        if lAmt > rAmt:
          r -= 1
        else:
          l += 1
    
    return ans 