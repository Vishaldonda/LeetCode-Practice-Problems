def is_match(s: str, p: str) -> bool:
    # Create a 2D DP array with dimensions (len(s) + 1) x (len(p) + 1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty string and empty pattern match
    dp[0][0] = True
    
    # Initialize for patterns like a*, a*b*, a*b*c* which can match empty string
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Consider zero occurrence of the element before '*'
                dp[i][j] = dp[i][j - 2]
                # Consider one or more occurrences of the element before '*'
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    
    # The result is whether the entire string s matches the pattern p
    return dp[len(s)][len(p)]

# Test cases
print(is_match("aa", "a"))      # Output: False
print(is_match("aa", "a*"))     # Output: True
print(is_match("ab", ".*"))     # Output: True
