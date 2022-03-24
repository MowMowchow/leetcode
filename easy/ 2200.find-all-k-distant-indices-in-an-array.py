class Solution:
  def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
    N = len(nums)
    vis = {}
    ans = []
    for i in range(N):
      if nums[i] == key:
        for j in range(i-k, i+k+1):
          if 0 <= j < N:
            if j not in vis:
              vis[j] = 1
              ans.append(j)
              
    return sorted(ans)