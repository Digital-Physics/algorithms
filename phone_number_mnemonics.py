# time(bounded by): O(n(4**n)(n)) my concatenation adds extra n, i think....
# + n(4**n) for just the string concatenations at the end
# space: O(n(4**n)) number of possibilities times the length of the possibilities
def phoneNumberMnemonics(phoneNumber):
    key_options = [["0"],
                   ["1"],
                   ["a", "b", "c"],
                   ["d", "e", "f"],
                   ["g", "h", "i"],
                   ["j", "k", "l"],
                   ["m", "n", "o"],
                   ["p", "q", "r", "s"],
                   ["t", "u", "v"],
                   ["w", "x", "y", "z"]]

    list_of_mnemonics = [[]]

    for i in phoneNumber:
        num = int(i)
        temp_bucket = []
        for partial_answer in list_of_mnemonics:
            print(num)
            for character in key_options[num]:
                # we don't mutate existing answer, so don't append
                new_partial_answer = partial_answer + [character]
                temp_bucket.append(new_partial_answer)
        # re-assign
        list_of_mnemonics = temp_bucket

    list_of_mnemonic_strings = []

    for mnemonic in list_of_mnemonics:
        string = "".join(mnemonic)
        list_of_mnemonic_strings.append(string)

    return list_of_mnemonic_strings



