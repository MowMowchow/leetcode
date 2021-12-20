class Solution:
  def minimumBuckets(self, street: str) -> int:
    N = len(street)
    
    hCnt = 0
    ans = 0
    
    if (N == 1 and street == "H") or street == "HH":
      return -1
    
    for i in range(N):
      if street[i] == "H":
        hCnt += 1
      elif hCnt > 0 and street[i] == ".":
        hCnt = 0
      if hCnt >= 3:
        return -1
      
    turn = False
    while len(street) > 0:
      if not turn and len(street) > 3:
        if street[:4] == ".H.H":
          ans += 1
          street = street[4:]
          turn = True
        
      if not turn and len(street) > 2:
        if street[:3] == "H.H":
          ans += 1
          street = street[3:]
          turn = True
      
      if not turn and len(street) > 1:
        if street[:2] == "H." or street[:2] == ".H":
          ans += 1
          street = street[2:]
          turn = True
      
      if not turn and len(street) == 1 and street == ".":
        street = ""
        turn = True
      
      if not turn and len(street) > 1 and street[0] == ".":
        street = street[1:]
        turn = True
        
      if not turn:
        return -1
      
      # print(street)
      turn = False
    
    
    
    
    
    return ans