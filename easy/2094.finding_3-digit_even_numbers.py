class Solution:
  def findEvenNumbers(self, digits: List[int]) -> List[int]:
    N = len(digits)
    ans = []
    dig = {}
    for digit in digits:
      if digit not in dig:
        dig[digit] = 1
      else:
        dig[digit] += 1
    
    
    for num in range(100, 1000):
      temp = dict(dig)
      sNum = str(num)
      i = int(sNum[0])
      j = int(sNum[1])
      k = int(sNum[2])
      
      if i in dig and j in dig and k in dig and num % 2 == 0:
        temp[i] -= 1
        temp[j] -= 1
        temp[k] -= 1
        
        if temp[i] >= 0 and temp[j] >= 0 and temp[k] >= 0:
          ans.append(num)

    
    return ans