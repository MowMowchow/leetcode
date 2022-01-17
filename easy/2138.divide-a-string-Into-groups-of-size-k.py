class Solution:
  def divideString(self, s: str, k: int, fill: str) -> List[str]:
    ans = []
    cnt = 1
    curr = ""
    k += 1
    while s:
      if cnt % k == 0:
        ans.append(str(curr))
        curr = ""
      else:
        curr += s[0]
        s = s[1:]
      cnt += 1
    
    k -= 1
    while not ((len(ans)*k + len(curr))%k == 0) and curr:
      curr += fill
    
    if len(curr) > 0:
      ans.append(curr)
    
    
    return ans