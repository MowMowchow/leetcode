class Solution:
  def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
    def gcd(a, b):
      return gcd(b, a%b) if b else a
    
    def isCoprime(a, b):
      return gcd(a, b) == 1
    
    def lcm(a,b):
        return (a // gcd(a,b))* b
    
    ans = list([nums.pop(0)])
    while nums:        
      if not isCoprime(nums[0], ans[-1]):
        curr = lcm(nums[0], ans[-1])
        nums[0] = curr
        ans.pop(-1)
      else:
        ans.append(nums.pop(0))
        
      if not ans:
        ans.append(nums.pop(0))
      
    return ans
    