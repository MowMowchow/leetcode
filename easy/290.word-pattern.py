#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    h1 = {}
    h2 = {}
    s = s.split(" ")
    s1 = ""
    s2 = ""
    for let in pattern:
      if let not in h1:
        h1[let] = len(h1)
      s1 += str(h1[let])
    
    for word in s:
      if word not in h2:
        h2[word] = len(h2)
      s2 += str(h2[word])

    return s1 == s2
# @lc code=end

