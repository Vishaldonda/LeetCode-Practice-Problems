import math
def reverse(x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = -x
            
        org_num = x
        rev_num = 0 
        while ( x > 0):
            rev_num *=10
            rev_num +=  x%10
            x //=10
            # print(rev_num)
            
        # print(rev_num)
        if rev_num > math.pow(2,31):
            return 0

        if flag: 
            return -rev_num

        return rev_num
    
print(reverse(321))