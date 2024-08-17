def myAtoi(s: str) -> int:

    # 1.Whitespace
    str = s.strip()

    if not str:
        return 0

    # 2.Signedness
    sign = 1
    if str[0] == '-':
        sign = -1
        str = str[1:] 
    elif str[0] == '+':
        str = str[1:] 

    # 3.conversion : string to an integer
    ind = 0
    end  = len(str)
    for i in range(len(str)):
        if not str[i].isdigit():
            end = i
            break

    
    str = str[ind:end]
    if not str:  # If there are no digits
        return 0

    # Output Formatting
    integer = int(str)*sign

    INT_MIN = -2**31
    INT_MAX = 2**31-1

    if integer <  INT_MIN:
        return INT_MIN

    if integer > INT_MAX:
        return INT_MAX

    return integer
    
str = "-00343fv43"
print(myAtoi(str))
