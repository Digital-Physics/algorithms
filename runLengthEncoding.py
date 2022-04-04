# time: O(n) since we go through the list once and don't concatenate strings but append to a list
# space: O(n) worst since we build up 2 chars per each char not in a sequence
def runLengthEncoding(string):
    symbol_counter = 1
    output_list = []

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            symbol_counter += 1
            # write under one of these circumstances
            if symbol_counter == 10:
                output_list.append(str(9))
                output_list.append(string[i - 1])
                symbol_counter = 1
        else:  # single symbols
            output_list.append(str(symbol_counter))
            output_list.append(string[i - 1])
            symbol_counter = 1

    # last character in string; we aren't accumulating a count anymore so write
    output_list.append(str(symbol_counter))
    output_list.append(string[-1])

    return "".join(output_list)

print(list(range(3)))
# for i in range(1,1) will just skip over the for loop and not error
print(list(range(1,1)))