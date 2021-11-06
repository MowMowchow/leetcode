class WordDistance:

    def __init__(self, wordsDict: List[str]):
      self.N = len(wordsDict)
      self.words = {}
      for i in range(self.N):
        if wordsDict[i] not in self.words:
          self.words[wordsDict[i]] = [i]
        else:
          self.words[wordsDict[i]].append(i)
      
      
    def shortest(self, word1: str, word2: str) -> int:
      w1N = len(self.words[word1])
      w2N = len(self.words[word2])
      low = float("inf")
      c1 = 0
      c2 = 0
      
      while c1 < w1N and c2 < w2N:
        low = min(low, abs(self.words[word1][c1]-self.words[word2][c2]))
        
        if self.words[word1][c1] < self.words[word2][c2]:
          c1 += 1
        else:
          c2 += 1
      
      return low


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)