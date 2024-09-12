# Input: s = "()[]{}"
# Output: true

def isValid(s: str) -> bool:
    stack = []
    for char in s:
        
        if char == '(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif char == '{':
            stack.append('}')
        elif not stack or stack.pop()!=char:
            return False
            
    return not stack

s = "()[]{}"
print(isValid(s))    