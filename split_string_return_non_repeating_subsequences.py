def merge_the_tools(string: str, k: int) -> None:
    """print out the non repeating subsequences after splitting the string into substrings"""
    num_of_substrings = len(string)//k # we need an int, not a float for range()
    dict_of_sets = {i: set() for i in range(num_of_substrings)}

    for idx in range(num_of_substrings):
        substring = string[idx*k: (idx+1)*k]
        subseq = []
        for s_idx in range(k):
            if substring[s_idx] not in dict_of_sets[idx]:
                subseq.append(substring[s_idx])
                dict_of_sets[idx].add(substring[s_idx])
        print("".join(subseq))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)