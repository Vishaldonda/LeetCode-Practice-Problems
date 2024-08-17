from typing import List
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    nums.sort() # nlogn

    # print(nums)
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i - 1]:
                continue
        for j in range(i+1,len(nums)-2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j+1
            l = len(nums)-1
            while(k<l):
                sum = nums[i]+nums[j]+nums[k]+nums[l]
                if sum == target:
                    res.append([nums[i],nums[j],nums[k],nums[l]])
                    
                    while k < l and nums[k]==nums[k+1]:
                        k+=1
                    while k < l and nums[l]==nums[l-1]:
                        l-=1

                    k+=1
                    l-=1

                elif sum<target:
                    k+=1
                else:
                    l-=1

    return res

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]