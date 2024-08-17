# Input: x = 121
# Output: true

# 1.Converting into string
# def isPalindrome(x: int) -> bool:
#     num_str = str(x)
#     rev_str = num_str[::-1]
#     print(num_str,rev_str)
#     return num_str == rev_str

# 2. With out converting into String

def isPalindrome(x: int) -> bool:
    org_num = x
    rev_num = 0 
    while(x > 0):
        rev_num *= 10 
        rev_num+=x%10
        x//=10
    
    print(rev_num)
    return rev_num == org_num
        
    
n = 121
print(isPalindrome(n))




# -121-