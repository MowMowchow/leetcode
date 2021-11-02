class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    R = len(board)
    C = len(board[0]) 
    N = len(word)
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    
    def rec(x, y, cl):
      if cl == N:
        return True
      if not vis[y][x]:
        vis[y][x] = True

        for mx, my in moves:
          if 0 <= x+mx < C and 0 <= y+my < R:
            if board[y+my][x+mx] == word[cl] and not vis[y+my][x+mx]:
              res = rec(x+mx, y+my, cl+1)
              if res:
                return True
        
        vis[y][x] = False
      
      return False
    
    
    for i in range(C):
      for j in range(R):
        if board[j][i] == word[0]:
          vis = [[False for x in range(C)] for y in range(R)]
          res1 = rec(i, j, 1)
          if res1:
            return True
    
    return False