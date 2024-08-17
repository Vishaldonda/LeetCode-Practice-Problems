def romanToInt(s: str) -> int:
    
    roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    
    total = 0
    prev_val = 0

    for i in reversed(s):
        curr_val = roman_dict[i]
        
        if curr_val < prev_val:
            total-=curr_val
        else:
            total+=curr_val
        
        prev_val = curr_val
    
    return total

s = "LIVI"
num = romanToInt(s)
print(num)

    