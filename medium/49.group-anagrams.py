#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      N = len(strs)
      tups = {}
      ans = []
      for string in strs:
        temp = [0 for x in range(26)]
        for let in string:
          temp[ord(let)-ord('a')] += 1
          
        tup = tuple(temp)
        
        if tup not in tups:
          tups[tup] = len(ans)
          ans.append([string])
        else:
          ans[tups[tup]].append(string)
      
      return ans
   
# @lc code=end

