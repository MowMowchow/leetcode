class Bank:

  def __init__(self, balance: List[int]):
    self.balance = [0]+balance
    self.N = len(self.balance)
  def transfer(self, account1: int, account2: int, money: int) -> bool:
    if 0 < account1 <= self.N and 0 < account2 <= self.N:
      if self.balance[account1] >= money:
        self.balance[account2] += money
        self.balance[account1] -= money
        return True
      
    return False

  def deposit(self, account: int, money: int) -> bool:
    if 0 < account <= self.N:
      self.balance[account] += money
      return True
    return False


  def withdraw(self, account: int, money: int) -> bool:
    if 0 < account <= self.N:
      if money <= self.balance[account]:
        self.balance[account] -= money
        return True
    return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)