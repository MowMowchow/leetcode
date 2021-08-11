#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
  def isPalindrome(self, s: str) -> bool:
    mapp = {'0':0, '1': 0, '2': 0, '3': 0, '4':0, '5': 0, '6': 0, '7':0, '8': 0, '9': 0, 'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0,
      'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 
      't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
    
    ss = ""
    for i in s:
      if i.lower() in mapp:
        ss += i.lower()
    
    N = len(ss)
    NH = N//2

    for i in range(NH):
      if ss[i] != ss[N-i-1]:
        return False
      
    return True
        
# @lc code=end

