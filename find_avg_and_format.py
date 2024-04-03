if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() # that's a nifty unpacking
        scores = list(map(float, line))  # use a list comprehension instead
        student_marks[name] = scores
    query_name = input()

    # print the average
    student_scores_list = student_marks[query_name]
    print(f"{sum(student_scores_list)/len(student_scores_list):.2f}")