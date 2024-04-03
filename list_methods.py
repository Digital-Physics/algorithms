if __name__ == '__main__':
    N = int(input())

    lst = []
    command_list = []

    for _ in range(N):
        command_list.append(input().split(" "))

    # we could also use these strings as keys and values could be lambda functions
    # we think of lambda as being a functional programming concept with no state outside what's passed in
    # but python lambdas seem to be able to reference variables not passed, so we didn't have to pass command_list to mutate it
    for command in command_list:
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif command[0] == "append":
            e = int(command[1])
            lst.append(e)
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "reverse":
            lst.reverse()
        elif command[0] == "sort":
            lst.sort()
        else:
            print("no match?")

