#  longest palindromic substring in O(n) time using Manacher's Algorithm

def longest_palindrome(s):
    # Preprocess the string to handle both odd and even length palindromes
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # Array to store the length of the palindrome radius at each center
    center = 0
    right = 0

    for i in range(n):
        mirror = 2 * center - i  # The mirrored index of i around the center
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        # Try to expand the palindrome around center i
        a = i + p[i] + 1
        b = i - p[i] - 1
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1

        # Update the center and right boundary if the palindrome at i expands beyond the current right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Find the maximum palindrome in p
    max_len = max(p)
    center_index = p.index(max_len)
    
    # Extract the longest palindrome from the original string
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

# Example usage:
s1 = "abab"
print(longest_palindrome(s1))  # Output: "aba" or "bab"

# TC : O(n)



# Using DP
# def longest_palindrome(s):
#     n = len(s)
#     if n == 0:
#         return ""
    
#     # Initialize a 2D DP table with False values
#     dp = [[False] * n for _ in range(n)]
    
#     start = 0
#     max_len = 1
    
#     # All substrings of length 1 are palindromes
#     for i in range(n):
#         dp[i][i] = True
    
#     # Check for palindromes of length 2
#     for i in range(n-1):
#         if s[i] == s[i+1]:
#             dp[i][i+1] = True
#             start = i
#             max_len = 2
    
#     # Check for palindromes of length 3 or more
#     for length in range(3, n+1):  # length is the length of the substring
#         for i in range(n-length+1):
#             j = i + length - 1  # j is the end index of the substring
#             if s[i] == s[j] and dp[i+1][j-1]:
#                 dp[i][j] = True
#                 start = i
#                 max_len = length
    
#     # Return the longest palindromic substring
#     return s[start:start+max_len]

# # Example usage:
# s1 = "babad"
# print(longest_palindrome(s1))  # Output: "bab" or "aba"

# s2 = "cbbd"
# print(longest_palindrome(s2))  # Output: "bb"

# TC: O(n)^2 