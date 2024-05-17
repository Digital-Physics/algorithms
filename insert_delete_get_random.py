from random import choice

class RandomizedSet:
    """all methods must run in O(1).
    
    trick1: have list of values (for random.choice(self.list)) and a map/dict from val_to_idx
    trick2: swap with end before you pop() when removing for a O(1) .pop()
    
    """
    def __init__(self):
        self.values_to_idx = dict()
        self.values_list = []

    def insert(self, val: int) -> bool:
        if val not in self.values_to_idx:
            self.values_list.append(val)
            self.values_to_idx[val] = len(self.values_list) - 1
            return True
        else:
            return False 

    def remove(self, val: int) -> bool:
        if val in self.values_to_idx:
            idx = self.values_to_idx[val]

            # swap with end, then pop (for constant time pop)
            self.values_list[idx], self.values_list[-1] = self.values_list[-1], self.values_list[idx]
            self.values_list.pop()

            # update the val_to_idx map for the swapped value we keep
            self.values_to_idx[self.values_list[idx]] = idx
            # and delete the one we removed/popped
            del self.values_to_idx[val]

            return True
        else:
            return False

    def getRandom(self) -> int:
        # linear time, but we want O(1)
        # return choice(list(self.values_dict.keys()))
        return choice(self.values_list)

