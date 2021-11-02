class Solution:
  def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    ans = 0
    
    N = len(seats)
    M = len(students)
    
    seats.sort()
    students.sort()
    
    for i in range(N):
      ans += abs(seats[i]-students[i])
    
    return ans