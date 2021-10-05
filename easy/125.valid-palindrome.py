#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
  def isPalindrome(self, s: str) -> bool:
    newS = ""
    
    for let in s:
      if let.lower().isalnum():
        newS += let.lower()
    
    return newS == newS[::-1]
        
# @lc code=end

