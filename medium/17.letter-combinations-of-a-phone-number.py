class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    N = len(digits)
    ans = []
    lets = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    def dfs(ci, cs):
      nonlocal N
      if ci < N:
        for i in lets[int(digits[ci])-2]:
          dfs(ci+1, cs+i)
        
      else:
        ans.append(cs)
    
    dfs(0, "")
    
    return [] if len(ans) == 1 and ans[0] == "" else ans