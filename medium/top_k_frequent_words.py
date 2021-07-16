class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapp = {}
        freq = {}
        ks = []
        
        for word in words:
          if word not in mapp:
            mapp[word] = 1
          else:
            mapp[word] += 1
              
        for i in mapp:
          if mapp[i] not in freq:
            freq[mapp[i]] = [i]
          else:
            freq[mapp[i]].append(i)
        
        for i in freq:
          freq[i].sort()
          
        final = []
        
        for i in range(len(words), -1, -1):
          if i in freq:
            for j in freq[i]:
              final.append(j)

        return(final[:k])
          