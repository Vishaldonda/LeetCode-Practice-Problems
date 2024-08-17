# Input: s = "abcabcbb"
# Output: 3

# Approach 1 : Sliding window technique

def longest_substr1(str):
    max_len = 0
    start = 0 
    occur = set()
    
    for ele in str:
        while ele in occur:
            occur.remove(str[start])
            start+=1
        occur.add(ele)
        max_len = max(max_len,len(occur))
        print(occur)
    return max_len

# Approach 2 : Using dictionary to hold index
def longest_substr(str):
    max_len = 0
    start = 0 
    occur = {}
    
    for i,char in enumerate(str):
        if char in occur and occur[char]>=start:
            start = occur[char]+1
            
        occur[char] = i
        max_len = max(max_len,i-start+1)
    
    return max_len

# str = input()
str = "abcabcbb"
print(longest_substr(str))



# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(min(n, m)), where m is the size of the character set 