def searchRange(nums, target: int):
    def first_index(nums,target):
        l = 0 
        h = len(nums)-1
        pos  = -1
        while(l<=h):
            mid = (l+h)//2 
            if nums[mid]==target:
                pos = mid
                h = mid-1
            elif nums[mid]>target:
                h = mid-1
            else:
                l = mid+1
        
        return pos

    def second_index(nums,target):
        l = 0 
        h = len(nums)-1
        pos  = -1
        while(l<=h):
            mid = (l+h)//2 
            if nums[mid]==target:
                pos = mid
                l = mid+1
            elif nums[mid]>target:
                h = mid-1
            else:
                l = mid+1
        
        return pos

    f = first_index(nums,target)
    s = second_index(nums,target)

    return [f,s]
        
nums = [5,7,7,8,8,10]
target = 8
