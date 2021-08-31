class Solution:
  def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    arr = [0 for x in range(length+1)]
    for a, b, c in updates:
      arr[a] += c
      arr[b+1] -= c
      
    for i in range(1, length):
      arr[i] += arr[i-1]
    
    return arr[:length]