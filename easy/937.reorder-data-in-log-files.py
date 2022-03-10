class Solution: 
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    nLogs = len(logs)
    letLogs = []
    digLogs = []
    for log in logs:
      log = log.split()
      if log[-1].isnumeric():
        digLogs.append(" ".join(list(log)))
      else:
        letLogs.append(list([log[1:], log[0]]))
    
    letLogs.sort()

    return [ident+" "+" ".join(letLog) for letLog, ident in letLogs] + (digLogs)
          