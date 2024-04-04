# Errors detected during execution are called "exceptions" and they are "raised"
test_case_count = int(input())
test_cases = []

for _ in range(test_case_count):
    test_cases.append([val for val in input().split()])

for case in test_cases:
    num, denom = case

    try:
        print(int(int(num)/int(denom)))
    except ZeroDivisionError as e:
        print(type(e))
        print("Error Code:", e)
    except ValueError as e:
        print(type(e))
        print("Error Code:", e)


