#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        original_pow = n
        n = abs(n)
        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        
        return (result if original_pow > -1 else result**(-1))
        
# @lc code=end

    