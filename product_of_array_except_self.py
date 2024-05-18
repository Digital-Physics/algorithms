from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """returns product of each number in list except the ith number.
    must be done in linear time, O(n).

    first instinct: 1) get product 2) divide by ith number
    issue: what if one of the numbers is 0? 
    1) we can't divide by 0 on the 0 element
    2) we can't easily back out the 0 we for the overall product for the 0 element.    

    note: if there are 2 or more 0s, everything is 0.
    """
    zeros = False
    zero_counter = 0
    total_prod = 1
    prod_for_single_zero = 1

    for i in range(len(nums)):
        if nums[i] == 0:
            zeros = True
            zero_counter += 1
            # prod_for_single_zero = prod_for_single_zero
        else:
            prod_for_single_zero *= nums[i]
        
        total_prod *= nums[i]
    
    if zero_counter > 1:
        return [0] * len(nums)
    elif zero_counter == 1:
        output = []

        for i in range(len(nums)):
            if nums[i] != 0:
                output.append(int(total_prod/nums[i])) # don't forget, / or // both return a float
            else:
                output.append(prod_for_single_zero)
        
        return output
    else:
        output = []

        for i in range(len(nums)):
            output.append(int(total_prod/nums[i]))
        
        return output

if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf([-1, -1, 0, -3, -3]))