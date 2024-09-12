def search(nums, target: int) -> int:
    l = 0 
    h = len(nums)-1

    while(l<=h):
        mid = (l+h)//2

        if nums[mid]==target:
            return mid

        if nums[mid]>=nums[l]: # check if left is sorted
            if nums[l]<=target and target < nums[mid]:
                h = mid-1
            else:
                l = mid+1

        else:
            if nums[mid]<target and target<=nums[h]:
                l = mid+1
            else:
                h = mid-1

    return -1
    

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))







# Binary Search

# def binary_search(arr,target):
#     l = 0 
#     h = len(arr)-1
#     while(l<=h):
#         mid = (l+h)//2 
#         print(mid)
#         if arr[mid] == target:
#             return mid
#         elif arr[mid]>target:
#             h = mid-1
#         else:
#             l = mid+1
    
#     return -1

# arr = [1,2,3,4,5,6,7]
# print(binary_search(arr,3))

