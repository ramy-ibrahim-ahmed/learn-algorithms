import random


class RandomizedSet:

    def __init__(self):
        self.list = []  # List to store the elements
        self.HTable = {}  # Hashmap to store the element -> index mapping

    def insert(self, val):
        if val not in self.HTable:
            self.list.append(val)  # Append the value to the list
            self.HTable[val] = len(self.list) - 1  # Store its index in the hashmap
            return True
        return False

    def remove(self, val):
        if val in self.HTable:
            # Get the index of the element to remove
            index = self.HTable[val]
            # Move the last element to the index to be deleted
            last_val = self.list[-1]
            self.list[index] = last_val
            self.HTable[last_val] = index
            # Remove the last element from the list
            self.list.pop()
            # Remove the element from the hashmap
            del self.HTable[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self.list)  # Pick a random element from the list
