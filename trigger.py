# Controller Trigger
# ------------------------------
# Description:
# Controller Trigger Class related to data and function to Trigger input
# To be used together with the main Controller Class

# Version
# ------------------------------
# 0.0   -   Initial version
#           [25.06.2022] - Jan T. Olsen

# Import packages
import toolbox as Toolbox

# Trigger Class
# -----------------------------
# Based on Trigger-Data, assign values to members of Trigger Class
# with correct scaling obtained from Gamepad-Constant
class Trigger():
    """
    Trigger Class:
    Assign values to Trigger members based on incomming Trigger-Data
    Trigger values are calculated with correct scaling with data from Gamepad-Constants
    :param GAMEPAD_CONST: Controller Constants (Toolbox._GAMEPAD_CONST)
    :param TriggerData: Trigger Data (Toolbox.JoystickData)
    """
    # Class Constructor
    def __init__(self,
                name : str, 
                GAMEPAD_CONST : Toolbox._GAMEPAD_CONST) -> None:

        # Trigger Data
        self.triggerData = Toolbox.TriggerData

        # Class Variables
        self.name = name
        self.trigger = dict()
        self.Val = 0
        self.B1 = 0
        self.B2 = 0
        self.ScalingDataConstants = GAMEPAD_CONST.TRIGGER_SCALING

        # Call Update at Class construction
        self.update()
    
    # Update Joystick Value(s)
    def update(self) -> None:

        # Call internal get-function
        self.get_trigger()

        # Class dictionary
        self.trigger = {self.name + 'T'  : float("{:.2f}".format(self.Val)),
                        self.name + 'B1' : self.B1,
                        self.name + 'B2' : self.B2}


    # Get Trigger Back-Bumper No. 1 Value
    def get_button_B1(self) -> bool:
        # Get Button Value
        self.B1 = self.triggerData.B1

        # Function Return
        return self.B1

    # Get Trigger Back-Bumper No. 2 Value
    def get_button_B2(self) -> bool:
        # Get Button Value
        self.B2 = self.triggerData.B2

        # Function Return
        return self.B2

    # Get Trigger Axis Value
    def get_axis(self) -> float:
        # Scale Axis Value
        self.Val = Toolbox.scale_input_trigger(self.triggerData.VAL, self.ScalingDataConstants)

        # Function Return
        return self.Val    

    # Get Joystick Values
    def get_trigger(self) -> dict:
        # Call internal functions
        self.get_axis()
        self.get_button_B1()
        self.get_button_B2()

        # Function Return
        # return [self.Val, self.B1, self.B2]
        return self.trigger
