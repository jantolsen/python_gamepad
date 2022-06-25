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
import controller_toolbox as ControllerToolbox

# Trigger Class
# -----------------------------
# Based on Trigger-Data, assign values to members of Trigger Class
# with correct scaling obtained from Gamepad-Constant
class Trigger():
    """
    Trigger Class:
    Assign values to Trigger members based on incomming Trigger-Data
    Trigger values are calculated with correct scaling with data from Gamepad-Constants
    :param GAMEPAD_CONST: Controller Constants (ControllerToolbox._GAMEPAD_CONST)
    :param TriggerData: Trigger Data (ControllerToolbox.JoystickData)
    """
    # Class Constructor
    def __init__(self, 
                GAMEPAD_CONST : ControllerToolbox._GAMEPAD_CONST):

        # Trigger Data
        self.triggerData = ControllerToolbox.TriggerData

        # Class Variables
        self.TrigVal = 0
        self.B1 = 0
        self.B2 = 0

        self.ScalingDataConstants = GAMEPAD_CONST.TRIG_SCALING
        # self.Value_raw = self.triggerData.VAL

    #     # Update Joystick Values
    #     self.updateValues(self.joystickData)

    #     # Class Input(s):
    #     self.Value_raw = triggerData.VAL
    #     self.ScalingDataConstants = GAMEPAD_CONST.TRIG_SCALING

    #     # Class Variables
    #     self.TrigVal = 0
    #     self.B1 = 0
    #     self.B2 = 0

    #     # Update Joystick Values
    #     self.updateValues(triggerData)

    # # Update Trigger Values based on new Input data
    # def updateValues(self, triggerData : ControllerToolbox.TriggerData):
    #     # Update Class Inputs
    #     self.Value_raw = triggerData.VAL
    #     self.B1 = triggerData.B1
    #     self.B2 = triggerData.B2

    #     # Get Trigger Values
    #     self.getTrigger()

    # Get Trigger Back-Bumper No. 1 Value
    def getButton_B1(self):
        # Get Button Value
        self.B1 = self.triggerData.B1

        # Function Return
        return self.B1

    # Get Trigger Back-Bumper No. 2 Value
    def getButton_B2(self):
        # Get Button Value
        self.B2 = self.triggerData.B2

        # Function Return
        return self.B2

    # Get Trigger Axis Value
    def getAxis(self):
        # Scale Axis Value
        self.TriggerVal = ControllerToolbox.scaleTriggerInput(self.triggerData.VAL, self.ScalingDataConstants)

        # Function Return
        return self.TrigVal    

    # Get Joystick Values
    def getTrigger(self):
        # Call internal functions
        self.getAxis()
        self.getButton_B1()
        self.getButton_B2()

        # Function Return
        return [self.TrigVal, self.B1, self.B2]
