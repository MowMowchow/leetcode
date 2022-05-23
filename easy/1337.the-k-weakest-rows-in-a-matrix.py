class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    return [x[1] for x in sorted([[sum(mat[i]), i] for i in range(len(mat))])[:k]]