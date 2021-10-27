class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
      N = len(original)
      out = []
      c = 0
      if (n*m == N):
        for i in range(m):
          temp = []
          for j in range(n):
            if c < N:
              temp.append(original[c])
            c += 1
          if temp:
            out.append(temp)

        return out
      else:
        return []