#
# @lc app=leetcode id=1023 lang=python3
#
# [1023] Camelcase Matching
#

# @lc code=start
class Solution:
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    Q = len(queries)
    N = len(pattern)
    parts = []
    ans = [True for x in range(Q)]
    
    
    for q in range(Q):
      temp = str(pattern)
      word = queries[q]
      for let in range(len(word)):
        
        if temp:
          if word[let] == temp[0]:
            if len(temp) > 0:
              temp = temp[1:]
            else:
              temp = ""
          elif word[let].upper() == word[let]:
            temp = "-1"
            break
        
        elif word[let].upper() == word[let]:
          temp = "-1"
          break
      
      if temp:
        ans[q] = False
        
    
    return ans      
# @lc code=end

