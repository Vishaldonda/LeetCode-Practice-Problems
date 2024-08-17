# Input: s = "babad"
# Output: "bab"


# def longest_palidrome(str):
#     max_len = 0
#     max_str = str[0]
#     for i in range(len(str)-1):
#         for j in range(i+1,len(str)+1):
#             if j-i+1 > max_len and str[i:j+1]==str[i:j+1][::-1]:
#                 max_len = max(max_len,j-i+1)
#                 max_str = str[i:j+1]
#                 print(max_len,max_str)
#     return max_str

# s = "abab"
# print(longest_palidrome(s))

# TC : O(n)^3


# Approach 2. Expand around Center

def longest_palidrome(str):
    
    def expand(left,right):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1
            right += 1
        
        return str[left+1:right]
        
    max_str = ""
    for i in range(len(str)):
        pal_odd = expand(i,i)
        pal_even = expand(i,i+1)
        
        longer_pal = pal_odd if len(pal_odd)>len(pal_even) else pal_even
        print(f"o:{pal_odd},e:{pal_even},f:{longer_pal}")
        
        if len(longer_pal)>len(max_str):
            max_str = longer_pal
    
    return max_str

s = "ababc"
print(longest_palidrome(s))

# TC : O(n)^2

