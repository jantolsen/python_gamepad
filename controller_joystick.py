# Controller Joystick
# ------------------------------
# Description:
# Controller Joystick Class related to data and function to joystick input
# To be used together with the main Controller Class

# Version
# ------------------------------
# 0.0   -   Initial version
#           [25.06.2022] - Jan T. Olsen

# Import packages
import controller_toolbox as ControllerToolbox

# Joystick Class
# -----------------------------
# Based on Joystick-Data, assign values to members of Joystick Class
# with correct scaling obtained from Gamepad-Constant
class Joystick():
    """
    Jostick Class:
    Assign values to Joystick members based on incomming Joystick-Data
    Joystick values are calculated with correct scaling with data from Gamepad-Constants
    :param GAMEPAD_CONST: Controller Constants (ControllerToolbox._GAMEPAD_CONST)
    :param JoystickData: Joystick Data (ControllerToolbox.JoystickData)
    """
    # Class Constructor
    def __init__(self, 
                name : str, 
                GAMEPAD_CONST : ControllerToolbox._GAMEPAD_CONST):

        # Joystick Data
        self.joystickData = ControllerToolbox.JoystickData

        # Class Variables
        self.name = name
        self.joy = dict()
        self.X = float("{:.3f}".format(0.0))
        self.Y = 0.0
        self.PB = 0
        self.ScalingData = GAMEPAD_CONST.JOY_SCALING

        # Call Update at Class construction
        self.update()
    
    # Update Joystick Value(s)
    def update(self) -> None:
        
        # Call internal get-function
        self.getJoystick()

        # Class dictionary
        self.joy = {self.name + 'X' : float("{:.2f}".format(self.X)),
                    self.name + 'Y' : float("{:.2f}".format(self.Y)),
                    self.name + 'PB' : self.PB}

    # Get Joystick Pushbutton Value
    def getButton_PB(self) -> bool:
        # Get Button Value
        self.PB = self.joystickData.PB

        # Function Return
        return self.PB

    # Get Joystick Axis-X Value
    def getAxis_X(self) -> float:
        # Get and Scale Axis Value
        self.X = ControllerToolbox.scaleJoystickInput(self.joystickData.X, self.ScalingData)

        # Function Return
        return self.X    

    # Get Joystick Axis-Y Value
    def getAxis_Y(self) -> float:
        # Get and Scale Axis Value
        self.Y = ControllerToolbox.scaleJoystickInput(self.joystickData.Y, self.ScalingData)

        # Function Return
        return self.Y   
    
    # Get Joystick Axis Values
    def getAxes(self) -> float:
        # Call internal get axis value
        self.X = self.getAxis_X()
        self.Y = self.getAxis_Y()

        # Function Return
        return [self.X, self.Y]

    # Get Joystick Values
    def getJoystick(self) -> dict:
        # Call internal functions
        self.getButton_PB()
        self.getAxes()

        # Function Return
        return self.joy