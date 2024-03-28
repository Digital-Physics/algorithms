# time: O(n) we go through the string just once, not looking at each n-gram
# space: O(1) we are just accumulating totals
def minion_game(string: str) -> None:
    """winner of game where one person gets credit for n-grams that 
    start with vowels, and the other consonants"""
    # note: we don't need to actually look at the n-gram beyond the first letter (doesn't need to be quadratic)
    # note: we don't actually need to group them before adding them up
    vowels = "AEIOU"  # Y is not included in the game def

    player1 = "Kevin"
    player2 = "Stuart"
    player1score = 0
    player2score = 0

    for i, letter in enumerate(string):
        if letter in vowels:
            # if the letter is the last, it only gets counted for 1 n-gram
            # if the letter is first, it gets counted l times, because there are l n-grams where l is the len(string)
            player1score += len(string) - i
        else:
            player2score += len(string) - i

    if player1score > player2score:
        print(player1, player1score)
    elif player2score > player1score:
        print(player2, player2score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


