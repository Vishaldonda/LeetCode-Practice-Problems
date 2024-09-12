
def divide(dividend,divisor):
    sign = -1 if (dividend>=0 and divisor<0 ) or (dividend<0 and divisor>=0) else 1
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = len(range(0,dividend-divisor+1,divisor))
    if sign == -1:
        result *=-1
    
    MIN_VALUE =  -(2**31)
    MAX_VALUE = (2**31-1)
    
    result = max(result,MIN_VALUE)
    result = min(result,MAX_VALUE)
    
    return result


dividend = 10
divisor =3
print(divide(dividend,divisor))
