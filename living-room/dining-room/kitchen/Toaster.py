import os
import math
import random
import narrator

from narrator.Checkpoint import exists
from inventory import Acquire
from inventory.Item import FixtureSpec
from inventory.Item import Factory

class Toaster(FixtureSpec):

    def __init__(self):
        super().__init__()

    def use(self):
        seed = math.floor(
            random.random() * 10
        )
        if seed > 5:
            print("🍞 TOAST 🍞")
            Factory("Toast")
        else:
            print("Nothing happens.")

def main():
    n = narrator.Narrator()
    n.path.change({"act": 10, "scene": 0})
    n.narrate()

    t = Toaster()
    t.use()
    if exists(["Toast.py"]):
        Acquire("Toast.py")

if __name__ == "__main__":
    main()
