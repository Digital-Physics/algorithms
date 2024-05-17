from typing import List

def generateParenthesis(n: int) -> List[str]:
    """generate all possible parentheses given n sets of ()."""
    # look for the pattern; simple example
    # start with () for n = 1
    # n = 2: ["()()", "(())"] (we wrapped the previous lists, or we put at the end, or the beginning)
    # but we don't want duplicates

    # if n == 1:
    #     return ["()"]

    # solutions = {"()"}
    solutions = {""}

    # for i in range(2, n + 1):
    for i in range(1, n + 1):
        next_solutions = set() # we don't want duplicate strings; new var; don't mutate solutions while iterating over

        for solution in solutions:
            next_solutions.add("(" + solution + ")")
            next_solutions.add("()" + solution )
            next_solutions.add(solution + "()")
        
        solutions = next_solutions

    return list(solutions)

if __name__ == "__main__":
    print(generateParenthesis(1))
    print(generateParenthesis(2))
    print(generateParenthesis(3))





