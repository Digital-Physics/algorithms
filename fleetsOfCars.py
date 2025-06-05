# input: target = 12
# pos: [10, 8, 0, 5, 3]
# speed: [3, 1, 2, 1, 4]
# Faster Cars can't overtake cars; they merge and become one fleet.
# How many fleets of cars(1 or more) cross the target?
# https://www.youtube.com/shorts/0pqPalQbPdc
from typing import List

class Solution:
    def __init__(self):
        self.comment = "I didn't need to make this a class or initialize anything"

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_and_speed = list(reversed(sorted(zip(position, speed))))
        print(position_and_speed)

        # start with lead car and take one car at a time
        # look at the time for the lead car finishing
        lead_car_counter = 1 # we know first car will finish
        time_to_finish = (target - position_and_speed[0][0]) / position_and_speed[0][1]
        
        for i in range(1, len(position)):
            curr_finish = (target - position_and_speed[i][0]) / position_and_speed[i][1]

            if curr_finish > time_to_finish:
                lead_car_counter += 1
                time_to_finish = curr_finish

        return lead_car_counter
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.carFleet(12, [10, 8, 0, 5, 3], [3, 1, 2, 1, 4]))




         
        
