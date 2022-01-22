class Solution:
  def mostPoints(self, questions: List[List[int]]) -> int:
    N = len(questions)
    dp = [0 for x in range(N+1)]
    if N == 1:
      return questions[0][0]
    
    for i in range(N-1, -1, -1):
      score, skip = questions[i]
      if i+skip+1 <= N-1:
        dp[i] = max(dp[i], dp[i+skip+1]+score)
      if i+1 <= N-1:
        dp[i] = max(dp[i], dp[i+1], score)
      else:
        dp[i] = score
    return dp[0]
    
    
    