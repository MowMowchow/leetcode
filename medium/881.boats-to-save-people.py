class Solution:
  def numRescueBoats(self, people: List[int], limit: int) -> int:
    Np = len(people)
    ans = 0
    people.sort()
    
    l = 0
    r = Np-1
    
    while l <= r:
      if l < r:
        if people[l] + people[r] <= limit:
          ans += 1
          l += 1
          r -= 1
        else:
          ans += 1
          r -= 1
      elif l == r:
          ans += 1
          l += 1
          r -= 1
    
    return ans