#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    fN = len(flowerbed)
    
    for i in range(fN):
      if i == 0 and fN > 1:
        if flowerbed[i] == 0 and flowerbed[i+1] == 0:
          flowerbed[i] += 1
          n -= 1
      elif i == fN-1:
        if flowerbed[i] == 0 and flowerbed[i-1] == 0:
          flowerbed[i] += 1
          n -= 1
      else:
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
          flowerbed[i] += 1
          n -= 1
    
    return True if n <= 0 else False
    
# @lc code=end

