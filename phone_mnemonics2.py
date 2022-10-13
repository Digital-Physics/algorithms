class Mnemonic:
    def __init__(self, phone_num):
        self.key_options = [["0"],
        ["1"],
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"]]
        self.output = []
        self.phone_num = phone_num

    def mnemonics_helper(self, idx=0, partial=[0,0,0,0,0,0,0]):
        print("partial in class object", partial)
        if idx == len(self.phone_num):
            print("write to output attribute")
            solution = "".join(partial)
            self.output.append(solution)
        else:
            digit = self.phone_num[idx]
            letter_options = self.key_options[int(digit)]
            for letter in letter_options:
                print(idx)
                partial[idx] = letter
                self.mnemonics_helper(idx+1,partial)


mnemonic_obj = Mnemonic("2403170")
mnemonic_obj.mnemonics_helper()

print(mnemonic_obj.output)


# for recursive visualizer
def mnemonics(idx=0, phone_num="243", partial=[0,0,0], output=[]):
        print("idx", idx)
        print("output mutates between recursive calls", output)
        print("partial mutates too, but we only overwrite a letter once all possibilities are put in output (& are immutable)", partial)
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

        if idx == len(phone_num):
            solution = "".join(partial)
            output.append(solution)
        else:
            digit = phone_num[idx]
            letter_options = key_options[int(digit)]
            for letter in letter_options:
                partial[idx] = letter
                mnemonics(idx+1, phone_num, partial, output)


mnemonics()