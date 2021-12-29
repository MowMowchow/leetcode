class Solution:
  def kIncreasing(self, arr: List[int], k: int) -> int:
    N = len(arr)
    blocks = []
    ans = 0 
    
    for i in range(k):
      temp = []
      for j in range(i, N, k):
        temp.append(arr[j])
      blocks.append(temp)
    
    for block in blocks:
      N = len(block)
      temps = [0 for x in range(N+1)]
      tempMax = 0
      c = 1
      for i in range(N):
        if temps[0] > block[i]:
          temps[0] = block[i]
        elif temps[c-1] <= block[i]:
          temps[c] = block[i]
          c += 1
        else:
          l = 0
          r = c-1
          while l < r:
            mid = l+(r-l)//2
            if temps[mid] > block[i]:
              r = mid
            else:
              l = mid+1
              
          temps[l] = block[i]
      
      ans += N-(c-1)
            
    return ans