#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
  def nthUglyNumber(self, n: int) -> int:
    dp = [0 for x in range(3)]
    uh = [2, 3, 5]
    arr = [1]
    curr = 1
    
    for i in range(n):
      arr.append(min(arr[dp[0]]*2, arr[dp[1]]*3, arr[dp[2]]*5))
      
      for i in range(3):
        if arr[dp[i]]*uh[i] == arr[-1]:
          dp[i] += 1
    
    return arr[n-1]
       
# @lc code=end

