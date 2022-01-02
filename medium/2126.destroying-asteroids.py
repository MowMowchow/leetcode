class Solution:
  def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
    asteroids.sort()
    
    while asteroids:
      curr = asteroids.pop(0)
      if curr > mass:
        return False
      else:
        mass += curr
    
    return True
        