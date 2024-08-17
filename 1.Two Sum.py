# Input : [1,2,3,4,5] , k = 6
# Output : [1,3]
def two_sum(arr,k):
    ind = {}
    for i in range(len(arr)):
        if k-arr[i] in ind:
            return [ind[i],i]
        ind[arr[i]] = i
    return []

k = int(input("Enter K : "))
arr = list(map(int,input(" Enter Array :").split(' ')))

res  = two_sum(arr,k)
print(res)