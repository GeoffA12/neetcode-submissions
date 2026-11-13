class Solution:
    def isValid(self, s: str) -> bool:
        openingParentheses = {'(', '[', '{'}
        closingParentheses = {')', ']', '}'}
        stack = []
        l = list(s)

        for i in range(len(l)):
            ch = l[i]
            if ch in openingParentheses:
                stack.append(ch)
            
            else:
                if len(stack) == 0:
                    return False
                
                else:
                    val = stack.pop()

                    if ch == ')' and val != '(':
                        return False
                    elif ch == ']' and val != '[':
                        return False
                    elif ch == '}' and val != '{':
                        return False
                    
        if len(stack) == 0:
            return True
        else:
            return False