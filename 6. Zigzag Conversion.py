# Input: s = "PAYPALISHIRING", numRows = 3
# P   A   H   N
# A P L S I I G
# Y   I   R

# Output: "PAHNAPLSIIGYIR"

def convert(str,n):
    if n ==1 or n >len(str):
        return str
    
    rows = ['']*n
    curr_row = 0
    going_down = False
    
    print(rows)
    for char in str:
        rows[curr_row]+=char
        if curr_row == 0 or curr_row == n-1:
            going_down = not going_down
        
        curr_row += 1 if going_down else -1
        
            
    return ''.join(rows)

str = "PAYPALISHIRING"
n = 3
print(convert(str,n))