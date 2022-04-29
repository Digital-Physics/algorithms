# time: O(c1 + c2)
# space: O(c1 + c2)
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    print("block off time outside of daily bounds by adding a 'meeting'")
    block_out_off_hours(calendar1, dailyBounds1)
    block_out_off_hours(calendar2, dailyBounds2)
    print("eventually, we want take the 'union' or merge the two calendars to see openings.")
    print("but first we'll need to get the times out of the strings, and let's convert to minutes too (to have integers as a foundation)")
    converted_times1 = list(map(lambda x: [convert_time_to_minutes(x[0]), convert_time_to_minutes(x[1])], calendar1))
    converted_times2 = list(map(lambda x: [convert_time_to_minutes(x[0]), convert_time_to_minutes(x[1])], calendar2))
    print("converted cal times into int minutes:")
    print(converted_times1)
    print(converted_times2)
    merged_cal = merge_cals(converted_times1, converted_times2)
    print("merged flattened cals:")
    print(merged_cal)
    print("flatten the merged")
    flatten_merged_cal = flatten_overlap(merged_cal)
    print(flatten_merged_cal)
    print("get open slots:")
    return get_available_slots(flatten_merged_cal, meetingDuration)


def block_out_off_hours(calendar, dailyBounds):
    print("tip: use .insert and .append over list concatenation to save time")
    calendar.insert(0, ["0:00", dailyBounds[0]])
    calendar.append([dailyBounds[1], "24:00"])
    print("calendar after mutating it to block out off hours:")
    print(calendar)


def convert_time_to_minutes(time_str):
    print("time is converted from strings to int minutes")
    hours, minutes = list(map(lambda x: int(x), time_str.split(":")))
    print("the string", time_str, "is", hours * 60 + minutes, "minutes")
    return hours * 60 + minutes


def convert_minutes_to_time(minutes):
    print("minutes are converted from an int back into strings")
    print(minutes)
    hours = minutes // 60
    mins_remainder = minutes % 60
    if mins_remainder < 10:
        print(str(hours) + ":" + "0" + str(mins_remainder))
        return str(hours) + ":" + "0" + str(mins_remainder)
    else:
        print(str(hours) + ":" + str(mins_remainder))
        return str(hours) + ":" + str(mins_remainder)


def flatten_overlap(calendar):
    flattened = [calendar[0][:]]  # shallow copy
    print("to flatten, change the last ending time in the temp_output, or just add the block. increement either way.")
    for i in range(1, len(calendar)):
        if flattened[-1][1] >= calendar[i][0]:
            flattened[-1][1] = max(flattened[-1][1], calendar[i][1])
        else:
            flattened.append(calendar[i][:])
    return flattened


def merge_cals(converted_cal1, converted_cal2):
    print("should do merge sort...")
    print("first, looking at each stack. which top items starts first? that gives us the merge order.")
    print("increment i or j")
    merged_cal = []
    i, j = 0, 0

    while i < len(converted_cal1) and j < len(converted_cal2):
        print()
        print("merged:", merged_cal)
        print(converted_cal1)
        print(converted_cal2)
        if converted_cal1[i][0] <= converted_cal2[j][0]:
            merged_cal.append(converted_cal1[i])
            i += 1
        else:
            merged_cal.append(converted_cal2[j])
            j += 1

    while i < len(converted_cal1):
        print("first calendar/i leftover")
        merged_cal.append(converted_cal1[i])
        i += 1

    while j < len(converted_cal2):
        print("second calendar/j leftover")
        merged_cal.append(converted_cal2[j])
        j += 1

    return merged_cal


def get_available_slots(merged_flat_cal, meetingDuration):
    open_slots = []
    for i in range(1, len(merged_flat_cal)):
        if merged_flat_cal[i][0] - merged_flat_cal[i - 1][1] >= meetingDuration:
            start_time_str = convert_minutes_to_time(merged_flat_cal[i - 1][1])
            end_time_str = convert_minutes_to_time(merged_flat_cal[i][0])
            open_slots.append([start_time_str, end_time_str])
    return open_slots
