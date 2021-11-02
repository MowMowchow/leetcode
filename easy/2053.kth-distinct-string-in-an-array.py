class Solution:
  def kthDistinct(self, arr: List[str], k: int) -> str:
    vis = {}
    N = len(arr)
    cnt = 0
    for i in range(N):
      if arr[i] not in vis:
        vis[arr[i]] = 1
      else:
        vis[arr[i]] += 1
        
    for i in range(N):
      if vis[arr[i]] == 1:
        cnt += 1
      if cnt == k:
        return arr[i]
    return ""