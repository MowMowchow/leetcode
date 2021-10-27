class Solution:
    def areNumbersAscending(self, s: str) -> bool:
      N = len(s)
      arr = s.split(" ")
      N = len(arr)
      arr2 = []
      
      for i in range(N):
        if arr[i].isnumeric():
          arr2.append(int(arr[i]))
      
      good = True
      
      for i in range(1, len(arr2)):
        if arr2[i] <= arr2[i-1]:
          return False
      return True