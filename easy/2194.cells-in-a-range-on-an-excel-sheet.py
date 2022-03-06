class Solution:
  def cellsInRange(self, s: str) -> List[str]:
    N = len(s)
    ans = []
    
    for i in range(ord(s[3])-ord(s[0])+1):
      for j in range(int(s[4])-int(s[1])+1):
        ans.append(chr(ord(s[0])+i)+str(int(s[1])+j))
    
    return ans