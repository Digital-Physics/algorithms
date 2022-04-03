# time: O(nlog(n)) for the 2 sorting + n to traverse and compare two lists
# space: O(1) because sorting in place and going through lists one by one
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        redShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()

    blueShirtSpeeds.sort()
    running_total = 0

    for i in range(len(blueShirtSpeeds)):
        running_total += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return running_total