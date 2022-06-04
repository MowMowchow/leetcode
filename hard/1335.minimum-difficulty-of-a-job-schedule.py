class Solution:
  def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    N = len(jobDifficulty)
    dp = [[float("inf") for x in range(d+1)] for y in range(N+1)] # some value for considering the first i jobs and having j cuts left
    
    def rec(cJob, cSum, cutsLeft):
      if cJob > N or cutsLeft < 0: return
      if dp[cJob][cutsLeft] <= cSum: return
      if cJob > 0:
        dp[cJob][cutsLeft] = min(dp[cJob][cutsLeft], cSum)
        
      cMax = 0
      for job in range(cJob+1, N+1):
        cMax = max(cMax, jobDifficulty[job-1])
        rec(job, cSum+cMax, cutsLeft-1) # do a cut at job
      

    rec(0, 0, d)
      
    return dp[N][0] if dp[N][0] != float("inf") else -1
  
       