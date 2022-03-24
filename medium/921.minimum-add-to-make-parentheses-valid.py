class Solution:
  def minAddToMakeValid(self, s: str) -> int:
    N = len(s)
    o = 0
    c = 0
    for thing in s:
      if thing == "(":
        o += 1
      elif thing == ")":
        if not o:
          c += 1
        else:
          o -= 1
    
    return abs(o+c)
        