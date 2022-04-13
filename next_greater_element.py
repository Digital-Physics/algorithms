# two solutions here; Tim's version on the website is a more elegant coding of the second algorithm below; see that

# time: O(n**2)
# space: O(n)
def nextGreaterElement(array):
    output_array = []

    for i in range(len(array)):
        print(array, output_array)
        for d in range(len(array)):  # d for delta
            if array[(i + d) % len(array)] > array[i]:
                output_array.append(array[(i + d) % len(array)])
                break
        if len(output_array) == i:
            output_array.append(-1)

    return output_array


# time: O(n) using a stack
# space: O(n)
# start at end and keep stack
def nextGreaterElement2(array):
    if len(array) == 0:
        return []

    output_array = [None for _ in range(len(array))]
    stack = [array[-1]]

    print("array", array)
    print("first pass")
    for i in reversed(range(len(array) - 1)):
        print()
        print("idx", i, "of value", array[i])
        while stack:
            print("stack", stack)
            if array[i] < stack[-1]:
                # keep on stack and add more recent number
                output_array[i] = stack[-1]
                stack.append(array[i])
                print("output array updated", output_array)
                break
            else:
                stack.pop()
        stack.append(array[i])

    print()
    print("*********second pass*********")
    for i in reversed(range(len(array))):
        print()
        print("idx", i, "of value", array[i])
        if output_array[i] is None:
            while stack:
                print("stack", stack)
                if array[i] < stack[-1]:
                    output_array[i] = stack[-1]
                    stack.append(array[i])
                    print("output array updated", output_array)
                    break
                else:
                    stack.pop()
            if output_array[i] is None:
                output_array[i] = -1
                print("output array updated to reflect nothing found", output_array)
            stack.append(array[i])

    print("final output", output_array)
    return output_array
