class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
      N = len(answerKey)
      arr1 = [1 if answerKey[x] == "F" else 0 for x in range(N)]
      
      
      l = 0
      r = 0
      ans1 = 0
      curr = 0
      #print(a#rr1)
      while r < N:
        curr += arr1[r]
        
        if curr < k:
          ans1 = max(ans1, r-l+1)
          r += 1
        elif curr == k:
          ans1 = max(ans1, r-l+1)
          r += 1
        else:
          while curr > k:
            curr -= arr1[l]
            l += 1
          r += 1
          
      arr2 = [1 if answerKey[x] == "T" else 0 for x in range(N)]
      #prin#t(arr2)
      
      l = 0
      r = 0
      ans2 = 0
      curr = 0
      while r < N:
        curr += arr2[r]
        
        if curr < k:
          ans2 = max(ans2, r-l+1)
          r += 1
        elif curr == k:
          ans2 = max(ans2, r-l+1)
          r += 1
        else:
          while curr > k:
            curr -= arr2[l]
            l += 1
          r += 1
      
      return max(ans1, ans2)