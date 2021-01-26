class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s) % 2 == 1:
            return False
        for cb in s:
            if (cb == "("):
                stack.append(")")
        
            elif (cb == "["):
                stack.append("]")
        
            elif (cb == "{"):
                stack.append("}")
            
            elif (len(stack) > 0):
                print(cb, stack[-1])
                if (cb == stack[-1]):  # is a closing bracket
                   stack.pop(-1)
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True