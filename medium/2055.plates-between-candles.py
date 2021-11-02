class Solution:
  def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
    N = len(s)
    Q = len(queries)
    arr = [0 for x in range(N)]
    ans = [0 for x in range(Q)]
    
    between = False
    currAmt = 0
    for i in range(N):
      if s[i] == "|" and not between:
        between = True
        currAmt = 0
        if i > 0:
          arr[i] += arr[i-1]
      elif s[i] == "|" and between:
        between = True
        if i > 0:
          arr[i] += arr[i-1]
        arr[i] += currAmt
        currAmt = 0
      elif s[i] == "*" and between:
        currAmt += 1
        if i > 0:
          arr[i] += arr[i-1]
        
      else:
        currAmt = 0
        if i > 0:
          arr[i] += arr[i-1]
    
    nearest = [-1 for x in range(N)]
    
    for i in range(N-2, -1, -1):
      if s[i] == "|":
        nearest[i] = i
      else:
        nearest[i] = nearest[i+1]
            
    for q in range(Q):
      l = queries[q][0]
      r = queries[q][1]
      
      l = min(nearest[l], r)
      if l == -1:
        l = r
      
      ans[q] = arr[r]-arr[l]

    return ans
      
      
      