#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    N = len(words)
    charCnt = [len(word) for word in words]
    lines = []
    linesLength = []
    ans = []
    currLineLength = 0
    currLine = []
    ci = 0
    while ci < N:
      if currLineLength + charCnt[ci] == maxWidth or currLineLength + charCnt[ci] == maxWidth-1:
        currLineLength += charCnt[ci]
        currLine.append(words[ci])
        lines.append(list(currLine))
        linesLength.append(currLineLength)
        currLineLength = 0
        currLine = []
        ci += 1
          
      elif currLineLength + charCnt[ci] < maxWidth-1:
        currLineLength += charCnt[ci]
        currLine.append(words[ci])
        currLineLength += 1
        ci += 1
        
        if ci == N:
          lines.append(list(currLine))
          linesLength.append(currLineLength)
          currLineLength = 0
          currLine = []

      else:
        lines.append(list(currLine))
        linesLength.append(currLineLength-1)
        currLineLength = 0
        currLine = []
    

    for line in range(len(lines)):
      if line == len(lines)-1:  # last line case
        s = ""
        for word in range(len(lines[line])):
          if word == len(lines[line])-1:
            s += lines[line][word]
          else:
            s += lines[line][word] + " "
        
        leftoverSpaces = maxWidth-len(s)
        s += " "*leftoverSpaces
        ans.append(s)
        
      elif len(lines[line]) == 1:
        s = ""
        s += lines[line][0]
        leftoverSpaces = maxWidth-len(s)
        s += " "*leftoverSpaces
        ans.append(s)
        
      else:
        
        leftoverSpaces = maxWidth-linesLength[line]
        
        distributedSpaces = leftoverSpaces//(len(lines[line])-1)
        leftoverSpaces %= len(lines[line])-1
        s = ""
        for word in range(len(lines[line])):
          if word == len(lines[line])-1:
            s += lines[line][word]
          else:
            s += lines[line][word] + " "
            if distributedSpaces > 0:
              s += " "*distributedSpaces
            if leftoverSpaces > 0:
              s += " "
              leftoverSpaces -= 1
        
        ans.append(s)
            
    return ans  
# @lc code=end

