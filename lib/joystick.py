# Controller Joystick
# ------------------------------
# Description:
# Controller Joystick Class related to data and function to joystick input
# To be used together with the main Controller Class

# Version
# ------------------------------
# 0.1   -   Moved library files to designated folder
#           and updated Toolbox import
#           [30.06.2022] - Jan T. Olsen
# 0.0   -   Initial version
#           [25.06.2022] - Jan T. Olsen

# Import packages
import ctrl_toolbox as CtrlToolbox

# Joystick Class
# -----------------------------
# Based on Joystick-Data, assign values to members of Joystick Class
# with correct scaling obtained from Gamepad-Constant
class Joystick():
    """
    Joystick Class:
    Assign values to Joystick members based on incomming Joystick-Data
    Joystick values are calculated with correct scaling with data from Gamepad-Constants
    :param GAMEPAD_CONST: Controller Constants (CtrlToolbox._GAMEPAD_CONST)
    :param JoystickData: Joystick Data (CtrlToolbox.JoystickData)
    """
    # Class Constructor
    def __init__(self, 
                name : str, 
                GAMEPAD_CONST : CtrlToolbox._GAMEPAD_CONST):

        # Joystick Data
        self.joystickData = CtrlToolbox.JoystickData()

        # Class Variables
        self.name = name
        self.joy = dict()
        self.X = 0.0
        self.Y = 0.0
        self.PB = 0
        self.ScalingData = GAMEPAD_CONST.JOYSTICK_SCALING

        # Call Update at Class construction
        self.update()
    
    # Update Joystick Value(s)
    def update(self) -> None:
        
        # Call internal get-function
        self.get_joystick()

        # Class dictionary
        self.joy = {self.name + 'X' : float("{:.2f}".format(self.X)),
                    self.name + 'Y' : float("{:.2f}".format(self.Y)),
                    self.name + 'PB' : self.PB}

    # Get Joystick Pushbutton Value
    def get_button_PB(self) -> bool:
        # Get Button Value
        self.PB = self.joystickData.PB

        # Function Return
        return self.PB

    # Get Joystick Axis-X Value
    def get_axis_X(self) -> float:
        # Get and Scale Axis Value
        self.X = CtrlToolbox.scale_input_joystick(self.joystickData.X, self.ScalingData)

        # Function Return
        return self.X    

    # Get Joystick Axis-Y Value
    def get_axis_Y(self) -> float:
        # Get and Scale Axis Value
        self.Y = CtrlToolbox.scale_input_joystick(self.joystickData.Y, self.ScalingData)

        # Function Return
        return self.Y   
    
    # Get Joystick Axis Values
    def get_axes(self) -> tuple:
        # Call internal get axis value
        self.X = self.get_axis_X()
        self.Y = self.get_axis_Y()

        # Function Return
        return (self.X, self.Y)

    # Get Joystick Values
    def get_joystick(self) -> dict:
        # Call internal functions
        self.get_button_PB()
        self.get_axes()

        # Function Return
        return self.joy