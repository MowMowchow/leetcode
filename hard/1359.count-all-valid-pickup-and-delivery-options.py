class Solution:
  def countOrders(self, n: int) -> int:
    mod = 10**9 + 7 
    base = 1
    
    def f(i):
      nonlocal base
      if i == 1:
        return base
      temp = ((i % mod)*((2*i)-1)%mod) % mod
      base = temp*f(i-1)
      base %= mod
      
      return base

    
    return f(n)
      