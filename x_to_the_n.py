def myPow(x: float, n: int) -> float:
    """returns x**n
    Note: n can be a positive or negative int.
    If we did this w/ bin(n), it feels like we'd still want to use an exponent 
    like x**48 = (x**(2**5)*(x**(2**4)), so we won't do that."""

    def helper(x, n):
        print("we need to //2 until we hit base case, the build back up", n)
        if n == 0:
            return 1
        # elif n == 1: # not necessary, but we included it
        #     return x
        
        # we break it down recursively, and then build back up 
        temp = myPow(x, n // 2)
        temp = temp * temp
        

        # note that 5 and 4 will both get a recursive call of myPow(x, 2)
        if n % 2 == 1:
            print(n, "temp * temp * x:", temp * x)
            return temp * x
        else:
            print(n, "temp * temp:", temp)
            return temp
    
    # do it with positive numbers
    positive_answer = helper(x, abs(n))
    
    # handle positive or negative as a last step
    if n < 0:
        return 1 / positive_answer
    return positive_answer

def myPow2(x: float, n: int) -> float:
    def helper(x, n):
        print("we need to //2 until we hit base case, the build back up", n)
        if n == 1: # not necessary, but we included it
            return x
        
        temp = myPow(x, n // 2)
        temp = temp * temp
        
        if n % 2 == 1:
            print(n, "temp * temp * x:", temp * x)
            return temp * x
        else:
            print(n, "temp * temp:", temp)
            return temp
    
    # do it with positive numbers
    positive_answer = helper(x, abs(n))
    
    # handle positive or negative as a last step
    if n < 0:
        return 1 / positive_answer
    return positive_answer


def myPow3(x: float, n: int) -> float:
    def helper(x, n):
        # 2^11
        # 2^5 * 2^5 * 2
        # (2^2 * 2^2 * 2) (2^2 * 2^2 * 2) 2
        # ((2^1 * 2^1)(2^1 * 2^1)2)((2^1 * 2^1)(2^1 * 2^1)2)*2
        # 
        if n == 1: 
            return x
        
        if n % 2 == 1:
            return myPow3(x, n // 2) * myPow3(x, n // 2) * x
        else:
            return myPow3(x, n // 2) * myPow3(x, n // 2)
    
    # do it with positive numbers
    positive_answer = helper(x, abs(n))
    
    # handle positive or negative as a last step
    if n < 0:
        return 1 / positive_answer
    return positive_answer


if __name__ == "__main__":
    # print(myPow(2.0,2))
    # print(myPow(2.0,3))
    # print(myPow(2.0,4))
    # print(myPow(2.0,5))
    # print(myPow(2.0,6))
    print(myPow(2.0,11))
    print(myPow2(2.0,11))
    print("inefficient:")
    print(myPow3(2.0,11))