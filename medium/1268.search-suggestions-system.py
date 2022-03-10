class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    Np = len(products)
    Ns = len(searchWord)
    products.sort()
    ans = []
   
  
    def bs(x, pre):
      l, r = 0, Np
      while (l < r):
        mid = l+(r-l)//2
        if (x <= products[mid][:pre+1]):
          r = mid
        else:
          l = mid+1
      return l
    
    
    for i in range(Ns):
      temp = []
      ind = bs(searchWord[:i+1], i)
      for j in range(ind, min(ind+3, Np)):
        if searchWord[:i+1] == products[j][:i+1]: temp.append(products[j])
      ans.append(list(temp))
    
    return ans
      