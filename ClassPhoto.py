# time: O(nlogn) for two sorts + 2n for the second part
# space: O(1) because sort in place and going through list one at a time
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    length = len(redShirtHeights)

    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(1, length):
            if redShirtHeights[i] > blueShirtHeights[i]:
                return False
        return True
    elif redShirtHeights[0] > blueShirtHeights[0]:
        for i in range(1, length):
            if redShirtHeights[i] < blueShirtHeights[i]:
                return False
        return True
    else:
        return False