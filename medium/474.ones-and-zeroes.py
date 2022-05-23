class Solution:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    N = len(strs)
    dp = [[[0 for x in range(m+1)] for y in range(n+1)] for z in range(N+1)] # [str][1's][0's]
    ans = 0
    for i in range(N):
      one = 0
      zero = 0
      for let in strs[i]:
        if let == "1":
          one += 1
        else:
          zero += 1
      strs[i] = list([one, zero])    
      
    for i in range(1, N+1):
      for ni in range(n+1): # ones
        for mi in range(m+1): # zeroes
          if strs[i-1][0] <= ni and strs[i-1][1] <= mi:
            dp[i][ni][mi] = max(dp[i-1][ni][mi], dp[i-1][ni-strs[i-1][0]][mi-strs[i-1][1]]+1)
            
          else:
            dp[i][ni][mi] = dp[i-1][ni][mi]

      
    return dp[N][n][m]