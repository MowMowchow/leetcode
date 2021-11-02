class Solution:
  def nextBeautifulNumber(self, n: int) -> int:
    num = n+1
    while True:
      vis = {}
      
      s = str(num)
      ans = ""
      
      good = True
      for digit in s:
        if digit not in vis:
          if s.count(digit) == int(digit):
            vis[digit] = 1
          else:
            good = False
            break
      
      if good:
        return num
      else:
        num += 1