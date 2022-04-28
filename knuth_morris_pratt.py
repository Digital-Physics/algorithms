# substring search
# time O(n+m) not n*m!
# space: O(m) for our prefix=suffix encoder
def knuthMorrisPrattAlgorithm(string, substring):
    print("as you go through the string and are continuing to match on your target substring pattern...")
    print("is there a sequence of length 1-n that is not only a prefix but also a suffix?")
    print("...meaning you've seen two potential starting points for completing the pattern going forward")
    print("so after your two characters mismatch on the leading run...")
    print("we don't need to reset to the second letter in the string we are searching (like the naive O(mn) approach)")
    print("we can keep going unless we happen to have have just passed a prefix=suffix situation")
    print("jump back to where the matching prefix run left off and was growing...")
    print("note: KMP is O(m+n). It gets its speed from moving the index i in the string it is searching forward, not back")
    print("if that's the case, we should start rechecking in the pattern from where the prefix run left off.")
    print("check the subsequent letter against what we just stopped on. maybe they'll match.")
    print("if they match, we proceed as normal indexing i and j.")
    print("if they don't, we are again left with checking to see if this j follows a prefix=suffix string...some nesting going on here...")
    print()
    print("identifying this prefix=suffix property in the pattern is something we do ahead of time.")
    print("so let's compute and represent any repetitive prefix=suffix structure that may exist in the pattern/substring")
    prefix_suffix_encoder = [None for _ in substring]
    # i and j shift together when they match
    j = 0
    i = 1

    while i < len(substring):
        print()
        print("i,j", i, j)
        print("prefix=suffix encoder", prefix_suffix_encoder)
        if substring[i] == substring[j]:
            print("record in our encoder array the prefix=suffix end idx", i, "in our substring/pattern")
            prefix_suffix_encoder[i] = j
            i += 1
            j += 1
        elif j == 0:  # we didn't match last "time" (not just last i, but last nested time)
            print("There is no prefix up to index", i, "that is also a suffix.")
            print("Our prefix-suffix encoder stays None at index i, j remains 0, and i increments +1")
            i += 1
        else:
            print("Didn't match, but there is a prefix up to index", i, "that is also a suffix.")
            print("Let's pick up matching right after where the prefix left off.")
            if prefix_suffix_encoder[j - 1] is None:
                j = 0
            else:
                j = prefix_suffix_encoder[j - 1] + 1

    print("substring pattern & prefix_suffix_encoder:")
    print(string)
    print("the prefix ending at this index is also a suffix")
    print(prefix_suffix_encoder)

    str_idx = 0
    pattern_idx = 0

    print()
    print("do matching on string now which is algorithmically very similar. go until it's logically impossible to find a match.")
    while str_idx + len(substring) <= len(string) + pattern_idx:
        if string[str_idx] == substring[pattern_idx]:
            if pattern_idx == len(substring) - 1:
                print("found! we've matched until end of pattern")
                return True
            print("match; increment str_idx i & pattern_idx j")
            str_idx += 1
            pattern_idx += 1
        elif pattern_idx == 0:
            print("pattern_idx at 0. we can't jump back, so just increment str_idx i.")
            str_idx += 1
        else:
            print("jump back, if possible, and pick up after the matching prefix")
            if prefix_suffix_encoder[pattern_idx - 1] is None:
                pattern_idx = 0
            else:
                pattern_idx = prefix_suffix_encoder[pattern_idx - 1] + 1

    print("we got to the end of the string, with backtracks, and we still didn't find it.")
    return False