class Solution:
  def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
    arr = [0 for x in range(200010)]
    startPos += 1
    for x, y in fruits:
      arr[x+1] += y
    N = len(arr)
    ans = 0
    for i in range(1, N):
      arr[i] += arr[i-1]
      
    for i in range(k+1):
      ans = max(ans, arr[min(startPos+i, N-1)]-arr[min(startPos, max(startPos-(k-i*2)-1, 0))])    
    
    for i in range(k+1):
      ans = max(ans, arr[max(min(startPos+(k-i*2), N-1), startPos)]-arr[max(startPos-i-1, 0)])
    
    return ans