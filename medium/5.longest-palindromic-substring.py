#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
  def longestPalindrome(self, s: str) -> str:
    N = len(s)
    ans1 = [-1, ""]
    ans2 = [-1, ""]
    
    
    def doOdd():
      nonlocal ans1
      d = [0 for x in range(N)]
      l = 0
      r = -1
      
      for i in range(N):
        j = l+r-i
        k = 1 if i > r else min(d[j], r-i+1)
        
        while 0 <= i-k and i+k < N and s[i-k] == s[i+k]:
          k += 1
        
        d[i] = k
        k -= 1
        if d[i] > ans1[0]:
          ans1[0] = d[i]
          ans1[1] = s[i-d[i]+1:i+d[i]]
        if i+k > r:
          r = i+k
          l = i-k
          
    
    def doEven():
      nonlocal ans2
      d = [0 for x in range(N)]
      l = 0
      r = -1
      
      for i in range(N):
        j = l+r-i+1
        k = 0 if i > r else min(d[j], r-i+1)
        
        while 0 <= i-k-1 and i+k < N and s[i-k-1] == s[i+k]:
          k += 1
          
        d[i] = k
        k -= 1
        if d[i] > ans2[0]:
          ans2[0] = d[i]
          ans2[1] = s[i-d[i]:i+d[i]]
        if i+k > r:
          r = i+k
          l = i-k-1
    
    
    doOdd()
    doEven()
    
    return ans1[1] if ans1[0] > ans2[0] else ans2[1]
        
# @lc code=end

