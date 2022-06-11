'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.

EX1:
Input: s = "()"
Output: true

EX2:
Input: s = "()[]{}"
Output: true

EX3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.
'''    
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
