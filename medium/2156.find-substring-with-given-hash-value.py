class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        idx = 0
        prod = 0
        pow = 1
        for _ in range(k):
            prod += (ord(s[_])-ord('a')+1)*pow
            if _ != k-1: pow *= power
        
        while idx < n:
            #print(prod, "?")
            if prod%modulo == hashValue:
                return s[idx:idx+k]
            else:
                val = ord(s[idx])-ord('a')+1
                #print("removing", val, "at", idx)
                prod -= val
                prod //= power
                prod += (ord(s[idx+k])-ord('a')+1)*pow
                idx += 1
