from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    min_sum  = float('inf')
    min_target_sum = float('inf')

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i+1
        k = len(nums)-1
        while(j<k):
            sum = nums[i]+nums[j]+nums[k]
            target_sum = abs(target-sum)
            
            if sum == target:
                return target
            
            if target_sum < min_target_sum:
                min_target_sum = target_sum
                min_sum = sum
            
            elif sum < target:
                j+=1
                
            else:
                k-=1
                
    return min_sum

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums,target)) # (-1 + 2 + 1 = 2)


# target = 2

# num = [1,0,-1,4,-10]
# min_int = float('inf')
# for i in num:
#     print(abs(target-i))
#     if abs(i-target) < min_int:
#         min_int = abs(i-target)
        
# print(min_int)