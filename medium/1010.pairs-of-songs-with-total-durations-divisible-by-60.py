#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    N = len(time)
    freq = {}
    ans = 0
    
    for i in time:
      i %= 60
      if i not in freq:
        freq[i] = 1
      else:
        freq[i] += 1
    
    if 0 in freq:
      ans += ((freq[0]-1)*freq[0])//2
    
    if 30 in freq:
      ans += ((freq[30]-1)*freq[30])//2
    
    for i in range(1, 30):
      if i in freq and 60-i in freq:
        ans += freq[i]*freq[60-i]
    
    return ans
        
# @lc code=end

