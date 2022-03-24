class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    pushN = len(pushed)
    popN=  len(popped)
    possible = False
    temp = []
    
    while pushed or temp:
      if pushed:
        curr = pushed.pop(0)
        if curr == popped[0]:
          popped.pop(0)
        else:
          temp.append(curr)
          
      if temp:
        while temp:
          if temp[-1] == popped[0]:
            temp.pop(-1)
            popped.pop(0)
          else:
            break

      if not pushed:
        while temp:
          if temp[-1] == popped[0]:
            temp.pop(-1)
            popped.pop(0)
          else:
            break        
        if not popped: possible = True
        break
    

    return possible