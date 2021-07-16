class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        n = len(s)
        left = 0
        right = 0
        counter = 0
        curr = 0
        if s != "" and s != " ":
            while left <= right:
                if s[right] not in dic:
                    dic[s[right]] = True
                    curr += 1
                    right += 1
                    counter = max(counter, curr)

                    if right == n:
                        break

                else:
                    del dic[s[left]]
                    left += 1
                    curr -= 1

                counter = max(counter, curr)
                        
            return counter
        
        else:
            if s == " ":
                return 1
            else:
                return 0