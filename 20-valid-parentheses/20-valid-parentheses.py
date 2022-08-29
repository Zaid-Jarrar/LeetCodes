class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for par in s:
            
            if par in ["(",'{','[']:
                stack.append(par)
            
            elif par in [")",'}',']']:
                if len(stack) == 0:
                    return False
            
                elif par == ")" and stack[-1] == "(":
                    stack.pop()
                elif par == "]" and stack[-1] == "[":
                    stack.pop()
                elif par == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            
                
        if len(stack) > 0:
            return False
        return True
                    
                    
            
        