class Solution:
  def longestPalindrome(self, words: List[str]) -> int:
    freq = {}
    singles = {} # number of usable singles
    doubles = {}
    doublesList = []
    vis = {}
    ans = 0
    for word in words:
      if word not in freq:
        freq[word] = 0
      freq[word] += 1
      
    bestDouble = 0
    bestUsed = False
    
    for key in freq:
      if key[::-1] in freq and key[::-1] != key and key not in vis: # single
        vis[key] = 1
        vis[key[::-1]] = 1
        
        singles[key] = freq[key]
        singles[key[::-1]] = freq[key[::-1]]
        
        ans += min(freq[key], freq[key[::-1]])*4
      elif  key[::-1] in freq and key[::-1] == key: # double
        doubles[key] = freq[key]
    
    for key in doubles:
      doublesList.append(doubles[key])
    
    doublesList.sort(reverse=True)
    
    for val in doublesList:
      if not bestUsed and val % 2 == 1:
        ans += val*2
        bestUsed = True
      else:
        ans += 2*((val//2) * 2)
        
    return ans
    
    
    