# Controller Directional-Pad
# ------------------------------
# Description:
# Controller Directional-Pad Class related to data and function to Directional-Pad input
# To be used together with the main Controller Class

# Version
# ------------------------------
# 0.0   -   Initial version
#           [25.06.2022] - Jan T. Olsen

# Import packages
import toolbox as Toolbox

# Joystick Class
# -----------------------------
# Based on Directional-Pad-Data, assign values to members of Directional-Pad Class
# with correct scaling obtained from Gamepad-Constant
class DPad():
    """
    Directional-Pad Class:
    Assign values to Directional-Pad members based on incomming Directional-Pad-Data
    :param DPadData: D-Pad Data (Toolbox.DPadData)
    """
    # Class Constructor
    def __init__(self) -> None:

        # D-Pad Data
        self.dPadData = Toolbox.DPadData

        # Class Variables
        self.name = 'DPad_'
        self.dPad = dict()
        self.L = 0
        self.R = 0
        self.U = 0
        self.D = 0

        # Call Update at Class construction
        self.update()
    
    # Update Joystick Value(s)
    def update(self) -> None:

        # Call internal get-function
        self.getDPad()
        
        # Class dictionary
        self.dPad = {self.name + 'L' : self.L,
                    self.name + 'R' : self.R,
                    self.name + 'U' : self.U,
                    self.name + 'D' : self.D}

    # Get D-Pad Left-Button Value
    def getButtonLeft(self) -> bool:
        # Get Button Data
        self.L = self.dPadData.L

        # Function Return
        return self.L

    # Get D-Pad Right-Button Value
    def getButtonRight(self) -> bool:
        # Get Button Data
        self.R = self.dPadData.R

        # Function Return
        return self.R

    # Get D-Pad Up-Button Value
    def getButtonUp(self) -> bool:
        # Get Button Data
        self.U = self.dPadData.U

        # Function Return
        return self.U

    # Get D-Pad Down-Button Value
    def getButtonDown(self):
        # Get Button Data
        self.D = self.dPadData.D

        # Function Return
        return self.D

    # Get D-Pad Button Values
    def getDPad(self) -> dict:
        # Call internal functions
        self.getButtonLeft()
        self.getButtonRight()
        self.getButtonUp()
        self.getButtonDown()

        # Function Return
        # return [self.L, self.R, self.U, self.D]
        return self.dPad
