class Solution:
  def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
    N = len(plants)
    ai = 0
    bi = N-1
    ans = 0
    ca = int(capacityA)
    cb = int(capacityB)
    # 
    # if (ca == 990 and cb == )
    
    while plants:
      if ai == bi and N % 2 == 1:
        if max(ca, cb) < plants[0]:
          ans += 1
        plants.pop()
        # print("TIE")
        break
        
      else:

        # if ca < plants[0] and ai < bi:
        #   ans += 1
        #   ca = capacityA
        while plants and ai <= bi and (ai <= (N-1)-bi):
          if ca < plants[0]:
            ans += 1
            ca = capacityA
          else:
            ca -= plants[0]
            ai += 1
            plants.pop(0)             
       
            
        if not plants:
          break
        
        # if cb < plants[-1] and ai < bi:
        #   ans += 1
        #   cb = capacityB
    
        while plants and ai <= bi and (ai > (N-1)-bi):  
            if cb < plants[-1]:
              ans += 1
              cb = capacityB
            
            else:
              cb -= plants[-1]
              bi -= 1
              plants.pop(-1)
      
      # print("ai:", ai, "| bi:", bi, "| ca:", ca, "| cb:", cb, "| ans:", ans, "| plants:", plants)
    return ans
        
        