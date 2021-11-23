class RangeFreqQuery:

  def __init__(self, arr: List[int]):
    self.freq = {}
    self.N = len(arr)
    for i in range(len(arr)):
      if arr[i] not in self.freq:
        self.freq[arr[i]] = []
      self.freq[arr[i]].append(i)
      
    

  def query(self, left: int, right: int, value: int) -> int:
    if value in self.freq:
      l = bisect.bisect_left(self.freq[value], left)
      r = bisect.bisect_right(self.freq[value], right)
      return (r-l)
    else:
      return 0

    
    

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)