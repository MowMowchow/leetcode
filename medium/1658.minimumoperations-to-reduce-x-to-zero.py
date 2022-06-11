class Solution:
  def minOperations(self, nums: List[int], x: int) -> int:
    nums = [0]+nums
    N = len(nums)
    vis = {}
    ans = float("inf")
    for i in range(1, N):
      nums[i] += nums[i-1]
      
    for i in range(N):
      vis[x-nums[i]] = i
      if nums[N-1]-nums[i] in vis:
        ans = min(ans, vis[nums[N-1]-nums[i]] + (N-i-1))
      
      
    return -1 if ans == float("inf") else ans