def getArtisticPhotographCount2(N: int, C: str, X: int, Y: int) -> int:
    def one_way(n_s: int, c_s: str, x_s: int, y_s: int) -> int:
        count = 0

        for p_idx in range(n_s):
            if c_s[p_idx] == "P":
                for a_idx in range(p_idx + x_s, p_idx + y_s + 1):
                    if a_idx < n_s and c_s[a_idx] == "A":
                        for b_idx in range(a_idx + x_s, a_idx + y_s + 1):
                            if b_idx < n_s and c_s[b_idx] == "B":
                                count += 1

        return count
    
    #reverse = C[::-1]
    reverse = list(reversed(C))
    return one_way(N, C, X, Y) + one_way(N, reverse, X, Y)

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    pb_dict = {"P": "B", "B": "P"}
    count = 0

    for first_idx in range(N):
        if C[first_idx] in pb_dict:
            for a_idx in range(first_idx + X, first_idx + Y + 1):
                if a_idx < N and C[a_idx] == "A":
                    for second_idx in range(a_idx + X, a_idx + Y + 1):
                        if second_idx < N and C[second_idx] == pb_dict[C[first_idx]]:
                            count += 1

    return count

def XgetArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    def one_way(n_s: int, c_s: str, x_s: int, y_s: int) -> int:
        count = 0
        search_start = 0

        while search_start < n_s:
            found_p = False
            if c_s[search_start] == "P":
                for a_idx in range(search_start + x_s, search_start + y_s + 1):
                    if a_idx < n_s and c_s[a_idx] == "P" and not found_p:
                        found_p = True
                        search_start = a_idx
                    if a_idx < n_s and c_s[a_idx] == "A":
                        for b_idx in range(a_idx + x_s, a_idx + y_s + 1):
                            if b_idx < n_s and c_s[b_idx] == "P" and not found_p:
                                found_p = True
                                search_start = b_idx
                            if b_idx < n_s and c_s[b_idx] == "B":
                                count += 1

            if not found_p:
                search_start += 1

        return count
    
    #reverse = C[::-1]
    reverse = list(reversed(C))
    return one_way(N, C, X, Y) + one_way(N, reverse, X, Y)

def getArtisticPhotographCount_toDo(N: int, C: str, X: int, Y: int) -> int:
    """use pointers for start and end of list and move inwards? 
    count duplicate starts in one go? never move backwards in for loop?"""
    pass

if __name__ == "__main__":
    print(getArtisticPhotographCount(8, ".PBAAP.B", 1, 3))