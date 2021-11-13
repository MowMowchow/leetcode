class Solution:
  def countVowelSubstrings(self, word: str) -> int:
    N = len(word)
    vowels = ["a", "e", "i", "o", "u"]
    ans = 0
    for i in range(N-4):
      bad = False
      vis = {}
      for j in word[i:]:
        if j not in vowels:
          bad = True
        else:
          if j not in vis:
            vis[j] = 1
          
          if len(vis) == 5 and not bad:
            ans += 1
      
      # if not bad and len(vis) == 5:
      #   ans += 1
    
    return ans