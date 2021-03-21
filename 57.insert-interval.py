#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    final = []
    while len(intervals) > 1:
      if newInterval:
        if intervals[0][1] >= newInterval[0] :
          intervals[0][1] = max(intervals[0][1], newInterval[1])
          newInterval = []
      else:
        if intervals[0][1]  >= intervals[1][0]:
          intervals[0][1] = max(intervals[0][1], intervals[1][1)
          print('merge one', intervals)
        
      else:
        final.append(intervals[0])
        intervals[0] = list(intervals[1])
        print('cant merge', final, intervals)

        if len(intervals) <= 2:
          final.extend(intervals)
          print('break one', final, intervals)
          break

      if len(intervals) <= 2:
        final.extend(intervals)
        print('break two', final, intervals)
        break

      intervals.pop(1)

    print(final)
    return final
# @lc code=end

