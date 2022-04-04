# time: O(s); string length + constant 26 alphabet reads to dict
# space: O(s) because we build up the list of cypher text in a string before we "".join()
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cypher_dict = {}
    output_list = []  # before join

    for idx, char in enumerate(alphabet):
        cypher_dict[char] = alphabet[(idx + key) % 26]

    for i in range(len(string)):
        output_list.append(cypher_dict[string[i]])

    return "".join(output_list)
