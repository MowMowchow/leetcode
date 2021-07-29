#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    distinct = []
    reg = {}
    mapp = {}
    arr = [0 for x in range(20010)]
    final = 0
    
    for i in range(len(intervals)):
      x, y = intervals[i]
      if x not in reg:
        reg[x] = True
        distinct.append(x)
      if y not in reg:
        reg[y] = True
        distinct.append(y)
        
    distinct.sort()
    
    for i in range(len(distinct)):
      mapp[distinct[i]] = i+1
  
    for x, y in intervals:
      arr[mapp[x]] += 1
      arr[mapp[y]] -= 1
      
    for i in range(1, 20010):
      arr[i] += arr[i-1]
      final = max(final, arr[i])

    return final


# @lc code=end