# Median of the two sorted arrays with complexity - O(log (m+n))

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000




def median_function(arr):
    mid = len(arr)//2
    
    median = 0
    if len(arr)%2==0:
        median = (arr[mid]+arr[mid-1])/2
    else:
        median = arr[mid]
        
    return median
    
# Approach 1: Merge and Sort
def find_median1(nums1,nums2):
    merged = nums1+nums2
    merged.sort()
    print(merged)
    
    median = median_function(merged)
    
    return median

# Approach 2: Two-Pointer Method
def find_median2(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    tot_len = m+n
    half_len = tot_len//2
    i = j = 0
    prev = curr = 0
    
    # Continue moving the pointers until you have processed half of the total number of elements.
    for _ in range(half_len+1):
        prev = curr
        if i<m and (nums1[i]<nums2[j] or j>=n):
            curr = nums1[i]
            i+=1
        else:
            curr = nums2[j]
            j+=1
    
    if tot_len % 2 == 1:
        return curr
    
    return (prev + curr) / 2.0

nums1 = [1,3]
nums2 = [2,4]

# Approach 2: Two-Pointer Method
print(find_median2(nums1,nums2))

# Time Complexity
# O(n + m), where ‘n’ & ‘m’ are the sizes of the two arrays.

# Space Complexity
# O(1).

#--------
# Approach 1: Merge and Sort
# print(find_median1(nums1,nums2))

# Time Complexity
# In the worst case TC is O((n + m) * log(n + m)).

# Space Complexity
# O(n + m), where ‘n’ and ‘m’ are the sizes of the arrays.

