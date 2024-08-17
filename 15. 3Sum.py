# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# Approach 2:
def threeSum(nums):
    res = []
    nums.sort() # nlogn

    # print(nums)
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i+1
        k = len(nums)-1
        while(j<k):
            sum = nums[i]+nums[j]+nums[k]
            if sum == 0:
                res.append([nums[i],nums[j],nums[k]])
                
                while j < k and nums[j]==nums[j+1]:
                    j+=1
                while j < k and nums[k]==nums[k-1]:
                    k-=1

                j+=1
                k-=1

            elif sum<0:
                j+=1
            else:
                k-=1

    return res

# TC : O(n^2)

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))









# # Approach 1 
# def threeSum(nums):
#     res = []
#     for i in range(len(nums)-2):
#         for j in range(i+1,len(nums)-1):
#             for k in range(j+1,len(nums)):
#                 if nums[i]+nums[j]+nums[k]==0:
#                     temp_list = [nums[i],nums[j],nums[k]]
#                     res.append(temp_list)

#     # print(res) # (O(n³))
    
#     remove_dup = set()
#     for ls in res:
#         remove_dup.add(tuple(sorted(ls)))
#     # print(remove_dup) # O(n*k*log(k))

#     result = []
#     for ele in remove_dup: 
#         result.append(ele)
#     # print(result) # O(m)
    
    
# TC : O(n^3)















# list = [1,2,3]
# print(list)

# list() function converts any iterable (such as strings, tuples, sets, dictionaries, ranges, or even generator objects) into a list.
# append()
# Functionality: Adds its argument as a single element to the end of the list.

# my_list.append([5, 6])  # Adds the entire list [5, 6] as a single element
# Output: [1, 2, 3, 4, [5, 6]]

# extend()
# Functionality: Iterates over its argument and adds each element to the list.
# my_list = [1, 2, 3]
# my_list.extend([4, 5])  # Adds each element of the list [4, 5] individually
# Output: [1, 2, 3, 4, 5]