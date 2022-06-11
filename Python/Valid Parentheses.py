class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup=[], { '(' : ')', '{' : '}', '[' : ']' }
        
        for char in s:
            if char in lookup.keys():
                stack.append(char)
            elif len(stack)==0 or lookup[stack.pop()] != char:
                return False
        
        return len(stack)==0  
print(Solution().isValid("()[]{}"))    
print(Solution().isValid("()[{]}")) 
