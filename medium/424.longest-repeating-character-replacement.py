#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    # two pointers for our current substring
    # - we may add a letter if:
    #   - (size of substring) - (the cnt letter with the max occurences in the substring) < k
    #   - the letter is = the letter with the max occurences in the substring
    #   - also update maxLet
    # - if we can't add a letter then we delete the leftmost letter of the substring until (size of substring) - (the cnt letter with the max occurences in the substring) < k
    #   - each time we delete a letter, we perform the following while making sure that the substring size >= 0:
    #     - iterate over the current substring's letters and recalculate the max occurence letter
    #       - if there is a tie we take the first max, unless there is a max where the letter is the same as the next one being added
    
    N = len(s)
    l = 0
    r = 0
    ans = 0
    curr = {}
    currSize = 0
    maxLet = [s[0], 1]  # letter, number of occurences

    for let in s:
      if let not in curr:
        curr[let] = 0


    while l <= r:
      if r == N:
        break

      if currSize - maxLet[1] < k or s[r] == maxLet[0]:  # we may add a letter
        currSize += 1
        curr[s[r]] += 1
        r += 1
        for let in curr:
          if curr[let] > maxLet[1]:
            maxLet[0] = let
            maxLet[1] = curr[let]

      else:
        while currSize - maxLet[1] >= k and currSize > 0:
          currSize -= 1
          curr[s[l]] -= 1
          if s[l] == maxLet[0]:
            maxLet[1] -= 1
          l += 1
          for let in curr:
            if curr[let] > maxLet[1]:
              maxLet[0] = let
              maxLet[1] = curr[let]
            elif curr[let] == maxLet[1] and let == s[r]:
              maxLet[0] = let
              maxLet[1] = curr[let]

      ans = max(ans, currSize)

    
    return ans
  
# @lc code=end

