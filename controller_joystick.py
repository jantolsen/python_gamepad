# Import packages
import controller_toolbox as ControllerToolbox
from dataclasses import dataclass

# Joystick Class
# -----------------------------
# Based on Joystick-Data, assign values to members of Joystick Class
# with correct scaling obtained from Gamepad-Constant
class Joystick():
    """
    Jostick Class:
    Assign values to Joystick members based on incomming Joystick-Data
    Joystick values are calculated with correct scaling with data from Gamepad-Constants
    :param GAMEPAD_CONST: Controller Constants (_GAMEPAD_CONST)
    :param JoyData: Joystick Data (_Joy_Data)
    """
    # Class Constructor
    def __init__(self, GAMEPAD_CONST : ControllerToolbox._GAMEPAD_CONST, 
                JoyData : ControllerToolbox._Joy_Data):

        # Class Input(s):
        self.X_raw = JoyData.X
        self.Y_raw = JoyData.Y
        self.PB = JoyData.PB
        self.JOY_SCALING = GAMEPAD_CONST.JOY_SCALING

        # Class Variables
        self.X = 0.0
        self.Y = 0.0
        self.PB = 0

        # Update Joystick Values
        self.updateValues(JoyData)

    # Update Joystick Values based on new Input data
    def updateValues(self, JoyData : ControllerToolbox._Joy_Data):
        # Update Class Inputs
        self.X_raw = JoyData.X
        self.Y_raw = JoyData.Y
        self.PB = JoyData.PB

        # Get Joystick Values
        self.getPushbuttonValue()
        self.getAxisValues()

    # Get Joystick Pushbutton Value
    def getPushbuttonValue(self):
        
        # Function Return
        return self.PB

    # Get Joystick Axis-X Value
    def getAxisXValue(self):
        # Scale Axis Value
        self.X = ControllerToolbox.scaleJoystickInput(self.X_raw, self.JOY_SCALING)

        # Function Return
        return self.X    

    # Get Joystick Axis-Y Value
    def getAxisYValue(self):
        # Scale Axis Value
        self.Y = ControllerToolbox.scaleJoystickInput(self.Y_raw, self.JOY_SCALING)

        # Function Return
        return self.Y   
    
    # Get Joystick Axis Values
    def getAxisValues(self):
        # Call internal get axis value
        self.X = self.getAxisXValue()
        self.Y = self.getAxisYValue()

        # Function Return
        return [self.X, self.Y]

    