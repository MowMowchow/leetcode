class Solution:
  def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    N = len(s)
    freq = {}
    lets = []
    for let in s:
      if let not in freq:
        freq[let] = 0
        lets.append(let)
      freq[let] += 1
      
      
    lets.sort(reverse=True)
    ans = ""
    i = 0
    while i < len(lets):
      repeated = False
      appended = False
      k = 1
      while freq[lets[i]] > 0 and ((not repeated and not appended) or (repeated and appended)):
        repeated = True
        appended = False
        appendAmt = min(repeatLimit, freq[lets[i]])
        freq[lets[i]] -= appendAmt
        ans += lets[i]*appendAmt
        
        if i < len(lets)-k:
          if freq[lets[i]] > 0 and freq[lets[i+k]] > 0 and lets[i] != lets[i+k]:
            freq[lets[i+k]] -= 1
            ans += lets[i+k]
            appended = True
            
            if freq[lets[i+k]] == 0:
              k += 1
        
      i += 1

    
    return ans
    