class Solution:
  def winnerOfGame(self, colors: str) -> bool:
    N = len(colors)
    As = 0
    Bs = 0
    j = 0
    
    while j < N:
      
      consec = True
      for i in range(j, N-1):
        if colors[j] == "A":
          if colors[i] == colors[i+1]:
            if i-j >= 1:
              As += 1
          else:
            j = int(i)
            # print("A break at", j)
            break
            
        elif colors[j] == "B":
          if colors[i] == colors[i+1]:
            if i-j >= 1:
              Bs += 1
          else:
            j = int(i)
            # print("B break at", j)
            break
        # print(As, Bs)
        if i == N-2:
          # print("end")
          j = int(i)
        
      j += 1
        
    
    # print(As, Bs)
    return True if As > Bs else False