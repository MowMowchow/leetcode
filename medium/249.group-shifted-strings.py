class Solution:
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    N = len(strings)
    sMap = {}
    
    for s in strings:
      diffs = []
      
      for i in range(1, len(s)):
        diffs.append(((ord(s[i])-ord(s[i-1]))+26)%26)
      
      temp = tuple(diffs)
      if temp not in sMap:
        sMap[temp] = []
        
      sMap[temp].append(s)
    
    ans = []
    for i in sMap:
      temp = []
      for s in sMap[i]:
        temp.append(s)
      ans.append(temp)

    return ans