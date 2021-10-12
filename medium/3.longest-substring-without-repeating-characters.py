#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    N = len(s)
    
    if N == 0:
      return 0
    
    l = 0
    r = 0
    ans = 1
    curr = {}
    
    for let in s:
      if let not in curr:
        curr[let] = 0
    
    
    while l <= r:  # r < N
      if r == N:
        break
      if curr[s[r]] == 0:
        curr[s[r]] += 1
        r += 1
      else:
        while curr[s[r]] > 0:
          curr[s[l]] = 0
          l += 1
      ans = max(ans, r-l)

    
    return ans
     
# @lc code=end

