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
import controller_toolbox as ControllerToolbox

# Joystick Class
# -----------------------------
# Based on Directional-Pad-Data, assign values to members of Directional-Pad Class
# with correct scaling obtained from Gamepad-Constant
class DPad():
    """
    Directional-Pad Class:
    Assign values to Directional-Pad members based on incomming Directional-Pad-Data
    :param DPadData: D-Pad Data (ControllerToolbox.DPadData)
    """
    # Class Constructor
    def __init__(self):

        # D-Pad Data
        self.dPadData = ControllerToolbox.DPadData

        # Class Variables
        self.L = 0
        self.R = 0
        self.U = 0
        self.D = 0

    #     # Update D-Pad Button Values
    #     self.updateValues(dPadData)

    # # Update D-Pad Values based on new Input data
    # def updateValues(self, dPadData : ControllerToolbox.DPadData):
    #     # Update Class Inputs
    #     self.L = dPadData.L
    #     self.R = dPadData.R
    #     self.U = dPadData.U
    #     self.D = dPadData.D

    # Get D-Pad Left-Button Value
    def getButtonLeft(self):
        # Get Button Data
        self.L = self.dPadData.L

        # Function Return
        return self.L

    # Get D-Pad Right-Button Value
    def getButtonRight(self):
        # Get Button Data
        self.R = self.dPadData.R

        # Function Return
        return self.R

    # Get D-Pad Up-Button Value
    def getButtonUp(self):
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
    def getDPad(self):
        # Call internal functions
        self.getButtonLeft()
        self.getButtonRight()
        self.getButtonUp()
        self.getButtonDown()

        # Function Return
        return [self.L, self.R, self.U, self.D]
