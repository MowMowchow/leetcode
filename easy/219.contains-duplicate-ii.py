#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vis = {}
        for i in range(len(nums)):
          if nums[i] in vis:
            if abs(vis[nums[i]]-i) <= k:
              return True
            else:
              vis[nums[i]] = i
          else:
            vis[nums[i]] = i
        return False

