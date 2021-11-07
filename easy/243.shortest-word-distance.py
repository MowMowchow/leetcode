class Solution:
  def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    word1Indexes = []
    word2Indexes = []
    ans = float("inf")
    N = len(wordsDict)
    
    for i in range(len(wordsDict)):
      if wordsDict[i] == word1:
        word1Indexes.append(i)
      elif wordsDict[i] == word2:
        word2Indexes.append(i)
    
    w1N = len(word1Indexes)
    w2N = len(word2Indexes)
    
    w1i = 0
    w2i = 0
    
    while w1i < w1N and w2i < w2N:
      ans = min(ans, abs(word1Indexes[w1i]-word2Indexes[w2i]))
      
      if word1Indexes[w1i] < word2Indexes[w2i]:
        w1i += 1
      else:
        w2i += 1
    
    return ans