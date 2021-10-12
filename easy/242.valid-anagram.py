#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    Ns = len(s)
    Nt = len(t)
    aS = [0 for x in range(26)]
    aT = [0 for x in range(26)]
    
    for let in s:
      aS[ord(let)-ord('a')] += 1  
    for let in t:
      aT[ord(let)-ord('a')] += 1
    
    return aS == aT 
    
# @lc code=end

