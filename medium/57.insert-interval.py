#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    final = []
    skip = False

    # before , after, merge front, merge back, consume new, consume curr, merge next
    while intervals:
      if newInterval[0] < intervals[0][0] and intervals[0][1] < newInterval[1]: # consume curr
        intervals[0][0] = newInterval[0]
        intervals[0][1] = newInterval[1]
        skip = True
      elif newInterval[0] <= newInterval[1] < intervals[0][0] and not skip: # before
        final.append(newInterval)
        skip = True
      elif newInterval[0] < intervals[0][0] <= newInterval[1] <= intervals[0][1]: # merge front
        intervals[0][0] = newInterval[0]  
        skip = True
      elif intervals[0][0] <= newInterval[0] <= intervals[0][1] <= newInterval[1]: # merge back
        intervals[0][1] = newInterval[1]  
        skip = True
      elif intervals[0][0] <= newInterval[0] <= newInterval[1] <= intervals[0][1]:
        skip = True 
      
      if len(intervals) > 1:
        if intervals[0][1] >= intervals[1][0]: # merge next
          intervals[0][1] = intervals[1][1]
          intervals.pop(1)
        else: # can't merge
          final.append(list(intervals[0]))
          intervals.pop(0)
      else: # only one left
        final.append(list(intervals[0]))
        if not skip and intervals[0][1] < newInterval[0]:
          final.append(newInterval)
        intervals.pop(0)
        


    return final if final else [newInterval]
# @lc code=end

