# Input: [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

def removElement(nums,val):
    
    ind = 0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[ind]=nums[i]
            ind+=1
    
    return ind
arr = [1,1,1,2,3,4,4] # Output: 2, nums = [2,2,_,_]
ind = removElement(arr,val=1)
print(arr,"index",ind) 