# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

def firstOccur(h: str, n: str) -> int:
    
    # O(n⋅m) 
    # ind = h.find(n)
    # return ind

    
    for i in range(len(h) - len(n) + 1):  #O(n)
        if h[i:i+len(n)] == n:           #O(m)
            return i
    return -1

n = "sadbutsad"
h = "sad"
print(firstOccur(n,h))

        