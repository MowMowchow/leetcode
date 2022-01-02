class Solution:
  def checkString(self, s: str) -> bool:
    pas = False
    for i in s:
      if i == "b":
        pas = True
      if pas and i == "a":
        return False
    
    return True