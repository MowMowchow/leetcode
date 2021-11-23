class Solution:
  def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    N = len(tickets)
    time = 0
    people = [[tickets[i], i] for i in range(N)]
    
    while True:
      tAmt, person = people.pop(0)
      tAmt -= 1
      time += 1
      if person == k and tAmt == 0:
        return time
      if tAmt > 0:
        people.append(list([tAmt, person]))