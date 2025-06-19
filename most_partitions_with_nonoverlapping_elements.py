def most_partitions(input_str: str) -> int:
    char_range = dict() # letter: min_idx, max_idx

    for i, char in enumerate(input_str):
        if char in char_range:  # Fixed: was "enumerate(char_range)"
            char_range[char][1] = i
        else:
            char_range[char] = [i, i]
    
    # Convert to list of ranges for easier processing
    ranges = list(char_range.values())
    
    # Sort ranges by start position
    ranges.sort(key=lambda x: x[0])
    
    # Union overlapping ranges
    merged_ranges = []
    for start, end in ranges:
        if merged_ranges and start <= merged_ranges[-1][1]:
            # Overlapping - merge with previous range
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
        else:
            # Non-overlapping - add new range
            merged_ranges.append([start, end])
    
    return len(merged_ranges)

def most_partitions2(input_str: str) -> int:
    max_idx = dict() # letter: max_idx
    partitions = 0

    for i, char in enumerate(input_str):
        max_idx[char] = i
    
    curr_partition_min_end = 0

    for i, char in enumerate(input_str):
        m = max_idx[char]
        if m >= curr_partition_min_end and i == m:
            partitions += 1
            # print("partition at", i, char)
            curr_partition_min_end = i + 1
        else:
            curr_partition_min_end = max(curr_partition_min_end, m)
    
    return partitions

if __name__ == "__main__":
    print(most_partitions("bobhaspepper"))
    print(most_partitions2("bobhaspepper"))