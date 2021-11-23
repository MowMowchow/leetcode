class Solution:
  def decodeCiphertext(self, encodedText: str, rows: int) -> str:
    if rows == 1:
      return encodedText
    
    cols = len(encodedText)//rows
    
    arr = []
    for row in range(rows):
      arr.append(encodedText[:cols])
      encodedText = encodedText[cols:]
    
    N = len(encodedText)
    cnt = 0
    ans = ""
    # print(rows, cols)
    for col in range(cols):
      for row in range(rows):
        if col+row < cols:
          ans += arr[row][col+row]
          cnt += 1
        
        if cnt == N:
          break
      
      if cnt == N:
        break
    
    if ans:
      while ans[-1] == " ":
        ans = ans[:-1]
        if not ans:
          break
      
    return ans