class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        vis = {}
        final = 0
        for i in nums:
            lengths[i] = 1
            
        for num in nums:
            if num not in vis:
                vis[num] =  True
                k = num-1
                if k in vis:
                    lengths[num] += lengths[k]
                else:
                    while k in lengths:
                        vis[k] = True
                        lengths[num] += lengths[k]
                        k -= 1
                        if k in vis:
                            lengths[num] += lengths[k]
                            break

                final = max(final, lengths[num])
        
        return final