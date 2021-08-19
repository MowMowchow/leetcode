#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ans = ""
        for i in nums:
            if cnt == 0:
               ans = i 
            cnt += -1 if i != ans else 1

        return ans

        
# @lc code=end

