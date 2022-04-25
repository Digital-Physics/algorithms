# time: O(n**2)
# space: O(n)
def minimumAreaRectangle(points):
    pairs_complement = {}
    min_area = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            print()
            # arbitrary but consistent ordering
            dict_key = order_points(points[i], points[j])
            if dict_key in pairs_complement:
                print("complement points for rectangle returned from dictionary")
                comp1, comp2 = pairs_complement[dict_key]
                print(comp1, comp2)
                area = calc_area(points[i], points[j], comp1, comp2)
                if area < min_area:
                    print("min area updated")
                    min_area = area
            else:
                print("complement points added to dictionary")
                comp1, comp2 = points_complement(points[i], points[j])
                comps_key = order_points(comp1, comp2)
                pairs_complement[comps_key] = [points[i], points[j]]

    return min_area if min_area != float("inf") else 0


def order_points(point1, point2):
    if hash(tuple(point1)) < hash(tuple(point2)):
        dict_key = (point1[0], point1[1], point2[0], point2[1])
    else:
        dict_key = (point2[0], point2[1], point1[0], point1[1])
    print("ordered dict key", dict_key)
    return dict_key


def calc_area(point1, point2, point3, point4):
    print("area based on 4 points", point1, point2, point3, point4)
    if point1[0] == point2[0]:
        height = abs(point1[1] - point2[1])
        width = abs(point1[0] - point3[0])
    elif point1[0] == point3[0]:
        height = abs(point1[1] - point3[1])
        width = abs(point1[0] - point2[0])
    elif point1[0] == point4[0]:
        height = abs(point1[1] - point4[1])
        width = abs(point1[0] - point2[0])
    print("w,h:", width, height)
    return width * height


def points_complement(point1, point2):
    point1_row = [point1[0], point2[1]]
    point2_row = [point2[0], point1[1]]
    print("points:", point1, point2)
    print("complements:", point1_row, point2_row)
    return point1_row, point2_row



