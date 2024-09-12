def removeDuplicates(arr):
    ind = 0
    for i in range(1,len(arr)):
        if arr[i]!=arr[ind]:
            ind+=1
            arr[ind]=arr[i]
        
    print("distinct digits :",arr[:ind+1])

arr = [1,1,1,2,3,4,4] # OUTPUT: [1,2,3,4,_,_,_] strating k digits should be unique
removeDuplicates(arr)
print(arr)
