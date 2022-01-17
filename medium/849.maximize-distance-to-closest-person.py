#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
  def maxDistToClosest(self, seats: List[int]) -> int:
    N = len(seats)
    ans = 0
    prev = 0
    N += 1
    seats.append(N)
    
    for i in range(1, N+1):
      if seats[i-1]:
        ans = max(ans, (i-prev)//2 if prev != 0 and seats[i-1] != N else i-prev-1)
        prev = i
    
    return ans
# @lc code=end

