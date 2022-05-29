class Solution:
    def maxProduct(self, words: List[str]) -> int:
      N = len(words)
      freq = []
      ans = 0
      
      for word in words:
        alp = [0 for x in range(26)]
        for let in word:
          alp[ord(let)-ord('a')] += 1
        
        tempTup = tuple(alp)
        freq.append(tempTup)
        
      for i in range(N):
        for j in range(i+1, N):
          flag = True
          for k in range(26):
            if freq[i][k] > 0 and freq[j][k] > 0:
              flag = False
              break
          if flag:
            ans = max(ans, len(words[i])*len(words[j]))
      
      return ans
    
      
      
        