#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
class Solution:
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    N = len(startTime)+1
    arr = [list([startTime[x], endTime[x], profit[x]]) for x in range(N-1)]
    arr.append([float("inf"), float("inf"), 0])
    dp = [0 for x in range(N+1)]
    arr.sort(key=lambda x: x[0])
    startTime.sort()
    
    def bs(x):
      l = 0
      r = N-1
      while l < r:
        mid = l+(r-l)//2
        if arr[mid][0] >= x:
          r = mid
        else:
          l = mid+1
      return l
    

    for i in range(N-2, -1, -1):
      ind = bs(arr[i][1])
      dp[i] = max(dp[i+1], arr[i][2]+dp[ind])

    return dp[0] 

# @lc code=end

