# compress a string of ints
from itertools import groupby

inp = [*input()]

print(*[(len(list(g)), int(k)) for k, g in groupby(inp)])


