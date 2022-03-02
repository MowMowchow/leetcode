class Bitset:

  def __init__(self, size: int):
    self.arr = [0 for x in range(size)]
    self.cnt = 0
    self.flips = False

  def fix(self, idx: int) -> None:
    if not self.flips and not self.arr[idx]:
      self.arr[idx] += 1
      self.cnt += 1
    elif self.flips and self.arr[idx]:
      self.arr[idx] -= 1
      self.cnt -= 1

  def unfix(self, idx: int) -> None:
    if not self.flips and self.arr[idx]:
      self.arr[idx] -= 1
      self.cnt -= 1
    elif self.flips and not self.arr[idx]:
      self.arr[idx] += 1
      self.cnt += 1

  def flip(self) -> None:
    self.flips = not self.flips

  def all(self) -> bool:
    return self.cnt == len(self.arr) if not self.flips else (len(self.arr)-self.cnt == len(self.arr))

  def one(self) -> bool:
    return self.cnt > 0 if not self.flips else self.cnt != len(self.arr)

  def count(self) -> int:
    return self.cnt if not self.flips else len(self.arr)-self.cnt

  def toString(self) -> str:
    if not self.flips:
      return "".join([str(x) for x in self.arr])
    elif self.flips:
      return "".join([str(1 if x == 0 else 0) for x in self.arr])

    



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()