def add_strings(s1: str, s2: str) -> str:
    """add nums that are too big for ints and are represented as strings"""      
    carry_digit = 0
    i_1 = len(s1) - 1
    i_2 = len(s2) - 1
    output = []

    while i_1 > -1 or i_2 > -1 or carry_digit > 0:
        num1 = 0 if i_1 < 0 else int(s1[i_1])
        num2 = 0 if i_2 < 0 else int(s2[i_2])

        value = num1 + num2 + carry_digit

        if value > 9:
            carry_digit = 1
            output.append(str(value - 10))
        else:
            carry_digit = 0
            output.append(str(value))

        i_1 -= 1
        i_2 -= 1

    output.reverse()

    return "".join(output)

if __name__ == "__main__":
    print(add_strings("123", "1000"))