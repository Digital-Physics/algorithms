if __name__ == '__main__':
    # time complexity: O(n) which is less than sorting O(n*log(n))
    n = int(input())
    # a list comprehension is nicer, in our opinion
    # and we don't want a map object, we want a list for the .remove() method. 
    # update: no we don't want to use remove() in this situation, but we'll leave the list comprehension regardless
    # arr = map(int, input().split())
    arr = [int(val) for val in input().split()]

    max_val = max(arr)
    # arr.remove(max_val)  # this only removes the first instance of the value, not all of them like they want
    one_less_list = [val for val in arr if val != max_val]
    print(max(one_less_list))