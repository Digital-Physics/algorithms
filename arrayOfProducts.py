# time: O(n) two passes but order of n
# space: O(n)
def arrayOfProducts(array):
    output_array = [1 for _ in range(len(array))]
    left_pass_running_product = 1
    right_pass_running_product = 1

    for i in range(len(array)):
        output_array[i] *= left_pass_running_product
        left_pass_running_product *= array[i]

    for i in range(len(array) - 1, -1, -1):
        output_array[i] *= right_pass_running_product
        right_pass_running_product *= array[i]

    return output_array
