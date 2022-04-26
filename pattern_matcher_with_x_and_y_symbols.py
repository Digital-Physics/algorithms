# time: O(m*n)? n=len(string) m=len(pattern)
# space: O(n+m)? for the chunks
def patternMatcher(pattern, string):
    print("pattern", pattern)
    print("string", string)

    length = len(string)
    print("length of str", length)
    xy_dict = {"x": 0, "y": 0}
    first_letter = pattern[0]
    found = False
    first_diff = None

    print()
    print("count x's and y's in pattern; also note length of first run of numbers")
    for i in range(len(pattern)):
        xy_dict[pattern[i]] += 1
        if pattern[i] != first_letter and not found:
            first_diff = i
            found = True

    print("counts", xy_dict)
    # get upper bound of search by assuming the other number is length 1
    if first_letter == "x":
        first_chunk_lim = (length - xy_dict["y"] * 1) // xy_dict["x"]
    else:
        first_chunk_lim = (length - xy_dict["x"] * 1) // xy_dict["y"]

    print()
    print("length limit, based on linear formula, of first-pattern-letter correspondence:", first_chunk_lim)
    for i in range(1, first_chunk_lim + 1):
        potential_first_xy = string[:i]
        print()
        print("potential first chunk", potential_first_xy)

        print("calc the implied length of the second chunk")
        if first_diff is not None:
            if first_letter == "x":
                # implied y length
                implied_length = (length - xy_dict["x"] * i) // xy_dict["y"]
            else:
                # implied x length
                implied_length = (length - xy_dict["y"] * i) // xy_dict["x"]
        else:
            implied_length = 0

        print("potential other chunk:")
        if first_diff is not None:
            start_idx = first_diff * i
            second_chunk = string[start_idx:start_idx + implied_length]
            print(second_chunk)

        print("create string using the above assumptions for x and y")
        chunks = [potential_first_xy]

        for i in range(1, len(pattern)):
            if pattern[i] == first_letter:
                chunks.append(potential_first_xy)
            else:
                chunks.append(second_chunk)

        print("implied list of chunks", chunks)

        if "".join(chunks) == string:
            if first_diff is not None:
                print("solution!!:", potential_first_xy, second_chunk)
                return [potential_first_xy, second_chunk] if first_letter == "x" else [second_chunk, potential_first_xy]
            else:
                return [potential_first_xy, ""] if first_letter == "x" else ["", potential_first_xy]
    return []




