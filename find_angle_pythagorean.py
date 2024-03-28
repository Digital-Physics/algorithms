# import numpy as np
import math

a = float(input())
b = float(input())

length_MC = ((a**2 + b**2)**(1/2))/2 # see hackerrank diagram of triangle
length_AC = (a**2 + b**2)**(1/2)

# arccos is the inverse of cos; answers are in radians, so converted to degrees
# print(int(np.arccos(length_MC/b)/(2*math.pi)*360))
# print(f"{round(math.acos(length_MC/b)/(2*math.pi)*360)}{chr(176)}")
# print(f"{90-round(math.asin(length_MC/b)/(2*math.pi)*360)}{chr(176)}")
# print(f"{round(math.asin(length_MC/b)/(2*math.pi)*360)}{chr(176)}")
print(f"{round(math.acos(b/length_AC)/(2*math.pi)*360)}{chr(176)}")