# time: O(n)
# space: O(1)
# more complicated than Clement's
# could find all peak points by seeing if i-1 < i > i+1 for each el, then expand peak, then max
def longestPeak(array):
    waiting_to_rise = True
    rising = False
    falling_after_rising = False
    peak_counter = 1
    best = 0

    for i in range(1, len(array)):
        if waiting_to_rise:
            if array[i] > array[i - 1]:
                waiting_to_rise, rising, falling_after_rising = False, True, False
                peak_counter += 1
        elif rising:
            if array[i] == array[i - 1]:
                waiting_to_rise, rising, falling_after_rising = True, False, False
                peak_counter = 1
            elif array[i] > array[i - 1]:
                peak_counter += 1
            else:
                waiting_to_rise, rising, falling_after_rising = False, False, True
                peak_counter += 1
        elif falling_after_rising:
            if array[i] == array[i - 1]:
                waiting_to_rise, rising, falling_after_rising = True, False, False
                if peak_counter > best:
                    best = peak_counter
                    peak_counter = 1
            elif array[i] > array[i - 1]:
                waiting_to_rise, rising, falling_after_rising = False, True, False
                if peak_counter > best:
                    best = peak_counter
                peak_counter = 2
            else:
                peak_counter += 1

    if falling_after_rising and peak_counter > best:
        return peak_counter
    else:
        return best