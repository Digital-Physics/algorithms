def reverse(x: int) -> int:
    """reverse integer. if the value is outside the allowable range, return 0
    32-bit signed ints have one space for pos/neg and 31 bits for the magnitude.
    therefore they range from 1 11111... to 0 111111... [-2**31, 2**31 - 1].

    Be care with negatives. 
    Numbers that end with 0 should be ok since int() will not include them.
    
    """

    if x > 0:
        x = int(str(x)[::-1])
    else:
        x = -int(str(x)[1:][::-1])

    if -(2**31) < x < (2**31) - 1:
        return x
    else:
        return 0
    

if __name__ == "__main__":
    print(reverse(310))
    print(reverse(-123))
    print(reverse(2**10))
    print(reverse(2**50))