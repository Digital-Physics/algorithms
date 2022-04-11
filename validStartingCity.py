# time: O(n)
# space: O(1)
def validStartingCity(distances, fuel, mpg):
    # can't start in a positive position where you need more gas because the distance is too far
    # need a starting city so that the sum over all future cities stays positive, until you wrap around
    # leverage the fact that the net gas will be 0 on the entire trip
    # if you start right after the low point in net miles gained, you will have just enough
    best_least_gas_entering_city = float("inf")
    running_total = 0

    for i in range(len(distances)):
        running_total += fuel[i] * mpg - distances[i]
        if running_total < best_least_gas_entering_city:
            best_least_gas_entering_city = running_total
            best_idx = i

    return (best_idx + 1) % len(distances)