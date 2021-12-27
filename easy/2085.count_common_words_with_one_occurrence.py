class Solution:
  def countWords(self, words1: List[str], words2: List[str]) -> int:
    N1 = len(words1)
    N2 = len(words2)
    ans = 0
    vis1 = {}
    vis2 = {}
    words = []
    for word in words1:
      if word not in vis1:
        vis1[word] = 1
        words.append(word)
      else:
        vis1[word] += 1
        
    for word in words2:
      if word not in vis2:
        vis2[word] = 1
        if word not in vis1:
          words.append(word)
      else:
        vis2[word] += 1
    for word in words:
      if word in vis1 and word in vis2:
        if vis1[word] == 1 and vis2[word] == 1:
          ans += 1

    return ans