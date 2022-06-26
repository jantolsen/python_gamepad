# Test Class
# ------------------------------
# Description:
# Test Class used for development

# Version
# ------------------------------
# 0.0   -   Initial version
#           [26.06.2022] - Jan T. Olsen

# Import packages
from cgi import test
import controller_toolbox as ControllerToolbox

# Test Class
# -----------------------------
# Based on Trigger-Data, assign values to members of Trigger Class
# with correct scaling obtained from Gamepad-Constant
class TestClass():

     # Class Constructor
    def __init__(self, name : str) -> None:
        
        self.val = 123
        self.B1 = 0
        self.B2 = 1    
        self.testDict = {name + 'T' : self.val, 
                        name + 'B1' : self.B1,
                        name + 'B2' : self.B2}

    def output(self) -> dict:
        return self.testDict


# Main Function
# ------------------------------   
if __name__ == '__main__':
    testClass = TestClass('R')

    out = testClass.output()

    print(out)

    print(out['RT'])


