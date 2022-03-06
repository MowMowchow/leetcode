class Solution:
  def uniqueLetterString(self, s: str) -> int:
    N = len(s)
    lets = [[0] for x in range(26)]
    
    for i in range(N):
      lets[ord(s[i].lower())-ord('a')].append(i+1)
    
    N += 1
    for i in range(26):
      lets[i].append(N)
    
    ans = 0  
    for let in range(26):
      nT = len(lets[let])
      for i in range(1, nT-1):
        ans += (lets[let][i]-lets[let][i-1])*(lets[let][i+1]-lets[let][i])
    
    return ans