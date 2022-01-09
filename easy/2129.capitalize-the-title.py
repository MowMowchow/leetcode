class Solution:
  def capitalizeTitle(self, title: str) -> str:
    ans = []
    words = title.split(" ")
    
    for word in words:
      if len(word) <= 2:
        ans.append(word.lower())
      else:
        ans.append(word[0].upper()+word[1:].lower())
        
    ans2 = ""
    for i in range(len(ans)):
      if i < len(ans)-1:
        ans2 += ans[i] + " "
      else:
        ans2 += ans[i]
    
    return ans2