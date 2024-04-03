# class EvenStream(object):
class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

# class OddStream(object):
class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

# default arguments are mutated and not redefined!!! They are evaluated once at definition time!
# https://docs.python-guide.org/writing/gotchas/
# We took one approach below. Another approach is to check for a None and create a new class object.
def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())

queries = int(input())
stream_params = []

for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    stream_params.append([stream_name, n])

for stream_param in stream_params:
    if stream_param[0] == "even":
        print_from_stream(stream_param[1])
    else:
        print_from_stream(stream_param[1], OddStream())
