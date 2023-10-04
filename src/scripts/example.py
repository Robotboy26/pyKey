# this import is needed it imports all of the functions that you can use from this project
from utils import *

# define what will happen when you trigger this macro (this function name has to be something that is not used in any other script files)
def example():
    keyboard.write("this is the basic example script")

# this is where you register the key that will trigger the script
keyboard.add_hotkey('l', example)

