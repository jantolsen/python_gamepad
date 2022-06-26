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
        self.name = 'Btn_'
        self.xboxButton = dict()
        self.A = 0        # Button - A
        self.B = 0        # Button - B
        self.X = 0        # Button - X
        self.Y = 0        # Button - Y
        self.Start = 0    # Button - Start
        self.Select = 0   # Button - Select

        

        # Call Update at Class construction
        self.update()
    
    # Update Joystick Value(s)
    def update(self) -> None:

        # Call internal get-function
        self.getButtons()

        # Class dictionary
        self.xboxButton = {self.name + 'A' : self.A,
                           self.name + 'B' : self.B,
                           self.name + 'X' : self.X,
                           self.name + 'Y' : self.Y,
                           self.name + 'Start'  : self.Start,
                           self.name + 'Select' : self.Select}

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
    def getButtons(self) -> dict:
        # Call internal functions
        self.getButtonA()
        self.getButtonB()
        self.getButtonX()
        self.getButtonY()
        self.getButtonStart()
        self.getButtonSelect()

        # Function Return
        return self.xboxButton
        # return [self.A, self.B, self.X, self.Y, self.Start, self.Select]

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
    def __init__(self, name : str) -> None:

        # D-Pad Data
        self.psButtonData = ControllerToolbox.PS_ButtonData

        # Class Variables
        self.name = 'Btn_'
        self.psButton = dict()
        self.Cross = 0       # Button - Cross
        self.Circle = 0      # Button - Circle
        self.Triangle = 0    # Button - Triangle
        self.Square = 0      # Button - Square
        self.Start = 0       # Button - Start
        self.Select = 0      # Button - Select

        # Call Update at Class construction
        self.update()
    
    # Update Joystick Value(s)
    def update(self) -> None:

        # Call internal get-function
        self.getButtons()

        # Class dictionary
        self.psButton = {self.name + 'Cross' : self.Cross,
                        self.name + 'Circle' : self.Circle,
                        self.name + 'Triangle' : self.Triangle,
                        self.name + 'Square' : self.Square,
                        self.name + 'Start'  : self.Start,
                        self.name + 'Select' : self.Select}

    # Get Button Cross Value
    def getButtonCross(self) -> bool:
        # Get Button Value
        self.Cross = self.psButtonData.Cross

        # Function Return
        return self.Cross

    # Get Button Circle Value
    def getButtonCircle(self) -> bool:
        # Get Button Value
        self.Circle = self.psButtonData.Circle

        # Function Return
        return self.Circle

    # Get Button Triangle Value
    def getButtonTriangle(self) -> bool:
        # Get Button Value
        self.Triangle = self.psButtonData.Triangle

        # Function Return
        return self.Triangle

    # Get Button Square Value
    def getButtonSquare(self) -> bool:
        # Get Button Value
        self.Square = self.psButtonData.Square

        # Function Return
        return self.Square

    # Get Button Start Value
    def getButtonStart(self) -> bool:
        # Get Button Value
        self.Start = self.psButtonData.Start

        # Function Return
        return self.Start

    # Get Button Select Value
    def getButtonSelect(self) -> bool:
        # Get Button Value
        self.Select = self.psButtonData.Select

        # Function Return
        return self.Select

    # Get Button Values
    def getButtons(self) -> dict:
        # Call internal functions
        self.getButtonCross()
        self.getButtonCircle()
        self.getButtonTriangle()
        self.getButtonSquare()
        self.getButtonStart()
        self.getButtonSelect()

        # Function Return
        # return [self.Cross, self.Circle, self.Triangle, self.Square, self.Start, self.Select]
        return self.psButton