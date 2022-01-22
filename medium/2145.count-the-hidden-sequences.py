class Solution:
  def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
    high = -float("inf")
    low = float("inf")
    curr = 0 
    ans = 0
    N = len(differences)
    for i in range(N):
      curr += differences[i]
      high = max(high, curr)
      low = min(low, curr)
    
    for i in range(lower, upper+1):
      if lower <= i+low <= upper and lower <= i+high <= upper:
        ans += 1
    
    return ans
  