#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    N1 = len(nums1)
    N2 = len(nums2)
    ans = []
    q = []
    p1 = 0
    p2 = 0
    
    heappush(q, [nums1[p1]+nums2[p2], p1, p2])
    
    while k > 0 and q:
      currSum, p1, p2 = heappop(q)
      ans.append([nums1[p1], nums2[p2]])
      
      if p2 == 0 and p1 < N1-1:
        heappush(q, [nums1[p1+1]+nums2[p2], p1+1, p2])
      if p2 < N2-1:
        heappush(q, [nums1[p1]+nums2[p2+1], p1, p2+1])
        
      k -= 1
      
    return ans  
    
# @lc code=end

