import operator

def person_lister(f): # decorator name, f is original function (e.g. name_format)
    def inner(people):
        people_list = []
        for person in people:
            people_list.append([f(person), person[2]])
        
        people_list.sort(key=lambda x: int(x[1]))
        
        return [val[0] for val in people_list]
        # return (f(person) for person in sorted(people, key=lambda x: x[2]))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')