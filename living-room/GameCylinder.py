import narrator

from Inventory.Item import FixtureSpec

class GameCylider(FixtureSpec):

    def __init__(self):
        super().__init__()

def main():
    n = narrator.Narrator()
    n.path.change({"act": 8, "scene": 0})
    n.narrate()

if __name__ == "__main__":
    main()
