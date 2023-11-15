# this import is needed it imports all of the functions that you can use from this project
import time
from utils import Key

# define what will happen when you trigger this macro (this function name has to be something that is not used in any other script files)
def example():
    print("Hello World")
    Key.write("this is the basic example script ")

# this is where you register the key that will trigger the script
# key options can be found here 
Key.addHotkey('o+p', example)

