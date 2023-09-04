import os
import gitit
import importlib
import inventory
import narrator

from narrator import Checkpoint
from inventory.Item import FixtureSpec

class Printer(FixtureSpec):

    def __init__(self):
        super().__init__()

    def write(self, document:str):
        try:
            mod = importlib.import_module(document)
            doc = mod.__name__
            with open(f"{doc}.md", "w") as fh:
                item = getattr(mod, document)()
                fh.write(item.__str__())
        except:
            print("PC LOAD LETTER\nPC LOAD LETTER\nPC LOAD LETTER")

    def use(self, document):
        self.write(document)

def main():

  n = narrator.Narrator()
  n.path.change({"act": 6, "scene": 0})
  
  if Checkpoint.check_flag("ink"):
    n.path.scene = 2
    gitit.get(file_name = "Lease.py")
    obj = Printer()
    obj.use("Lease")
    os.remove( 
      "Lease.py"
    )

  n.narrate()

if __name__ == "__main__":
  main()
