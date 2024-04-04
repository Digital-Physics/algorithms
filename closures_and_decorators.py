# decorators take in the original function and return a new wrapped function (which calls original)
# decorators are nested functions; 
#   the outer function is the decorator name; 
#   the inner is the new original-wrapped function you return

def my_decorator(original_func): 
    # The wrapper function is a closure that remembers original_func, the original sort_phone function
    def wrapped_function(matched_arg):  # wrapped function argument count should match original functions
        #  print("do something before, like start the clock, or in this case modify the input to be sorted")
        new_arg = [f"+91 {phone_num[-10:-5]} {phone_num[-5:]}" for phone_num in matched_arg]
        # [start:stop:step] => [val at index -10, -9, ... -1]  (stop is end of the list and step is 1 by default)
        original_func(new_arg) # call the original function
        #  print("do something after, like stop the clock")
    return wrapped_function

@my_decorator
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

# a call to sort_phone actually calls my_decorator(sort_phone)