# Controller Button
# ------------------------------
# Description:
# Controller Button Class related to data and function to Button input
# To be used together with the main Controller Class

# Version
# ------------------------------
# 0.0   -   Initial version
#           [25.06.2022] - Jan T. Olsen

# Import packages
import controller_toolbox as ControllerToolbox

# XBOX - Button Class
# -----------------------------
# Based on Button-Data, assign values to members of Button Class
# with correct scaling obtained from Gamepad-Constant
class XboxButton():
    """
    Xbox Button Class:
    Assign values to Button members based on incomming Button-Data
    :param XBOX_ButtonData: Xbox Button Data (ControllerToolbox.XBOX_ButtonData)
    """
    # Class Constructor
    def __init__(self):

        # D-Pad Data
        self.xboxButtonData = ControllerToolbox.XBOX_ButtonData

        # Class Variables
        self.A = 0        # Button - A
        self.B = 0        # Button - B
        self.X = 0        # Button - X
        self.Y = 0        # Button - Y
        self.Start = 0    # Button - Start
        self.Select = 0   # Button - Select

    #     # Update D-Pad Button Values
    #     self.updateValues(xboxButtonData)

    # # Update Button Values based on new Input data
    # def updateValues(self, xboxButtonData : ControllerToolbox.XBOX_ButtonData):
    #     # Update Class Inputs
    #     self.A = xboxButtonData.A
    #     self.B = xboxButtonData.B
    #     self.X = xboxButtonData.X
    #     self.Y = xboxButtonData.Y
    #     self.Start = xboxButtonData.Start
    #     self.Select = xboxButtonData.Select

    # Get Button A Value
    def getButtonA(self):
        # Get Button Value
        self.A = self.xboxButtonData.A

        # Function Return
        return self.A

    # Get Button B Value
    def getButtonB(self):
        # Get Button Value
        self.B = self.xboxButtonData.B

        # Function Return
        return self.B

    # Get Button X Value
    def getButtonX(self):
        # Get Button Value
        self.X = self.xboxButtonData.X

        # Function Return
        return self.X

    # Get Button X Value
    def getButtonY(self):
        # Get Button Value
        self.Y = self.xboxButtonData.Y

        # Function Return
        return self.Y

    # Get Button Start Value
    def getButtonStart(self):
        # Get Button Value
        self.Start = self.xboxButtonData.Start

        # Function Return
        return self.Start

    # Get Button Select Value
    def getButtonSelect(self):
        # Get Button Value
        self.Select = self.xboxButtonData.Select

        # Function Return
        return self.Select

    # Get Button Values
    def getButtons(self):
        # Call internal functions
        self.getButtonA()
        self.getButtonB()
        self.getButtonX()
        self.getButtonY()
        self.getButtonStart()
        self.getButtonSelect()

        # Function Return
        return [self.A, self.B, self.X, self.Y, self.Start, self.Select]

# PlayStation - Button Class
# -----------------------------
# Based on Button-Data, assign values to members of Button Class
# with correct scaling obtained from Gamepad-Constant
class PSButton():
    """
    PlayStation Button Class:
    Assign values to Button members based on incomming Button-Data
    :param PS_ButtonData: Xbox Button Data (ControllerToolbox.PS3_ButtonData)
    """
    # Class Constructor
    def __init__(self):

        # D-Pad Data
        self.psButtonData = ControllerToolbox.PS_ButtonData

        # Class Variables
        self.Cross = 0       # Button - Cross
        self.Circle = 0      # Button - Circle
        self.Triangle = 0    # Button - Triangle
        self.Square = 0      # Button - Square
        self.Start = 0       # Button - Start
        self.Select = 0      # Button - Select

    #     # Update D-Pad Button Values
    #     self.updateValues()

    # # Update Button Values based on new Input data
    # def updateValues(self, psButtonData : ControllerToolbox.PS_ButtonData):
    #     # Update Class Inputs
    #     self.Cross = psButtonData.Cross
    #     self.Circle = psButtonData.Circle
    #     self.Triangle = psButtonData.Triangle
    #     self.Square = psButtonData.Cross
    #     self.Start = psButtonData.Start
    #     self.Select = psButtonData.Select

    # Get Button Cross Value
    def getButtonCross(self):
        # Get Button Value
        self.Cross = self.psButtonData.Cross

        # Function Return
        return self.Cross

    # Get Button Circle Value
    def getButtonCircle(self):
        # Get Button Value
        self.Circle = self.psButtonData.Circle

        # Function Return
        return self.Circle

    # Get Button Triangle Value
    def getButtonTriangle(self):
        # Get Button Value
        self.Triangle = self.psButtonData.Triangle

        # Function Return
        return self.Triangle

    # Get Button Square Value
    def getButtonSquare(self):
        # Get Button Value
        self.Square = self.psButtonData.Square

        # Function Return
        return self.Square

    # Get Button Start Value
    def getButtonStart(self):
        # Get Button Value
        self.Start = self.psButtonData.Start

        # Function Return
        return self.Start

    # Get Button Select Value
    def getButtonSelect(self):
        # Get Button Value
        self.Select = self.psButtonData.Select

        # Function Return
        return self.Select

    # Get Button Values
    def getButtons(self):
        # Call internal functions
        self.getButtonCross()
        self.getButtonCircle()
        self.getButtonTriangle()
        self.getButtonSquare()
        self.getButtonStart()
        self.getButtonSelect()

        # Function Return
        return [self.Cross, self.Circle, self.Triangle, self.Square, self.Start, self.Select]