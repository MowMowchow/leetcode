class Solution:
  def maxTwoEvents(self, events: List[List[int]]) -> int:
    # print("!!!!!!!")
    best = 0
    N = len(events)
    events.sort(key=lambda x: x[0])
    rlMax = [x[2] for x in events]

    for i in range(N-2, -1, -1):
      rlMax[i] = max(rlMax[i+1], events[i][2])

    
    def bs(x):
      l = 0
      r = N-1   
      ans = -1
      while (l <= r):
        mid = (l + r) // 2
        if events[mid][0] <= x:
          l = mid + 1
        else:
          ans = mid;
          r = mid - 1

      return ans
 

    for i in range(N):
      res = bs(events[i][1])
      if res != -1:
        best = max(best, events[i][2]+rlMax[res])
      else:
        best = max(best, events[i][2])
      
    return best