class Solution:
  def maxScoreIndices(self, nums: List[int]) -> List[int]:
    N = len(nums)
    left = [0 for x in range(N+3)]
    right = [0 for x in range(N+3)]
    
    for i in range(N):
      if nums[i] == 0:
        left[i] += 1
      if i > 0:
        left[i] += left[i-1]
    
    for i in range(N-1, -1, -1):
      if nums[i] == 1:
        right[i] += 1
      if i < N-1:
        right[i] += right[i+1]
    
    ans = []
    best = -float("inf")
    
    for i in range(N+1):
      curr = 0 
      # if i > 0:
      curr += left[i-1]
      # if i < N-1:
      curr += right[i]
      # print(curr, best)
      if curr > best:
        ans = []
        best = curr
      if curr == best:
        ans.append(i)
    
    # print(left)
    # print(right)
    return ans