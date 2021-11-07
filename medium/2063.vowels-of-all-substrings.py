class Solution:
  def countVowels(self, word: str) -> int:
    cnt = 0
    arr = []
    N = len(word)
    vowels = {
      "a": 1,
      "e": 1,
      "i": 1,
      "o": 1,
      "u": 1
    }
    
    for i in range(N):
      if i == 0:
        arr.append(N)
      else:
        t1 = N-i
        t2 = arr[i-1]-i

        arr.append(t1+t2)
      
    for i in range(N):
      if word[i] in vowels:
        cnt += arr[i]
    
    return cnt