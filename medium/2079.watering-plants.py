class Solution:
  def wateringPlants(self, plants: List[int], capacity: int) -> int:
    N = len(plants)
    total = 0
    curr = int(capacity)
    plants = [[plants[x], x] for x in range(N)]
    
    while plants:
      currPlant, currDist = plants.pop(0)
      if curr >= currPlant:
        curr -= currPlant
        total += 1
      else:
        total += currDist*2
        curr = capacity
        plants = list([[currPlant, currDist]]) + plants
      
    return total
    