#
# @lc app=leetcode id=1884 lang=python3
#
# [1884] Egg Drop With 2 Eggs and N Floors
#

# @lc code=start
class Solution:
    def twoEggDrop(self, n: int) -> int:
      ans = -1
      l = 0
      r = n
      
      while l <= r:
        mid = l+(r-l)//2
        temp = (mid*(mid+1))//2
        if temp >= n:
          ans = mid
          r = mid-1
        else:
          l = mid+1

    	return ans

# @lc code=end

