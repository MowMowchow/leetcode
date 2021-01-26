class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] + 1 == 10:
            nine_total = 0
            for i in range(n-1, -1, -1):
                if (digits[i] == 9):
                    nine_total += 1
                else:
                    digits[n-nine_total-1] += 1
                    for i in range(n-nine_total, len(digits)):
                        digits[i] = 0
                    break
                if i == 0 and digits[i] == 9:
            # new length is n + (nine_total-1)
                    digits.append(0)            
                    digits[n-nine_total] = 1
                    for i in range(n-nine_total+1, len(digits)):
                        digits[i] = 0
                    break
                
        else:
            digits[-1] += 1
        return digits