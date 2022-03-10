class Solution:
  def minFlipsMonoIncr(self, s: str) -> int:
    N = len(s)
    leftZero = [0 for x in range(N+1)]
    rightOne = [0 for x in range(N+1)]
    ans = float("inf")
    
    leftZero[0] = 1 if not int(s[0]) else 0
    for i in range(1, N): leftZero[i] += (1 if not int(s[i]) else 0) + leftZero[i-1]
    rightOne[N-1] = int(s[N-1])
    for i in range(N-2, -1, -1): rightOne[i] += int(s[i]) + rightOne[i+1]
    
    for i in range(1, N):
      ans = min(ans, (i-leftZero[i-1])+((N-i)-rightOne[i]))
      
    return min(ans, leftZero[N-1], rightOne[0])