class Solution:
  def numberOfBeams(self, bank: List[str]) -> int:
    ans = 0
    N = len(bank)
    cnts = []
    for row in range(N):
      temp = 0
      for i in bank[row]:
        if i == "1":
          temp += 1
      if temp >= 1:
        cnts.append(temp)
    N = len(cnts)
    for i in range(1, N):
      ans += cnts[i-1]*cnts[i]
    return ans