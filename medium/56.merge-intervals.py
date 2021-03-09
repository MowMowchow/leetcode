#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort(key=lambda x: x[0])
      out = []
      while len(intervals) > 1:
        if intervals[0][1] >= intervals[1][0]:
          intervals[0][1] = max(intervals[1][1], intervals[0][1])
          intervals.pop(1)
        else:
          out.append(intervals[0])
          intervals.pop(0)

      out.append(intervals[0])

      return out

# @lc code=end

