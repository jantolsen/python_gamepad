# Controller
# ------------------------------
# Description:
# Read input values from external 
# handheld Controller

# Version
# ------------------------------
# 0.0   -   Initial version
#           [20.06.2022] - Jan T. Olsen

# Import packages
from logging import NullHandler
from inputs import get_gamepad
from inputs import devices
import threading
import controller_toolbox as ControllerToolbox
# import controller_toolbox2 as ControllerToolbox2

# Controller Class
# ------------------------------
class Controller():

    # Class constructor
    # ------------------------------
    def __init__(self):

        # Define Controller Members
        # (based on Dataclasses from Controller-Toolbox)
        self.Axis = ControllerToolbox._AxisData()
        self.Button = ControllerToolbox._ButtonData()

        # Search for connected controller
        # (using ControllerToolbox function)
        self.gamepad = ControllerToolbox.getController()

        # Determine the type of Controller
        # (using ControllerToolbox function)
        self.gamepad_type = ControllerToolbox.getControllerType()

        print(self.gamepad_type) 

        # Initialize Controller Monitor on a designated thread
        # ------------------------------
        # Based on the Controller-Type launch the related controller-monitor-thread

        # XBOX Controller
        if self.gamepad_type == 'XBOX':
            # Configure thread
            self._monitor_thread = threading.Thread(target=self._XBOX_ControllerMonitor, args=())
            self._monitor_thread.daemon = True

            # Start XBOX-Controller-Monitor
            self._monitor_thread.start()

        # Playstation 3 Controller
        elif self.gamepad_type == 'PS3':
            # Configure thread
            self._monitor_thread = threading.Thread(target=self._PS3_ControllerMonitor, args=())
            self._monitor_thread.daemon = True

            # Start PS3-Controller-Monitor
            self._monitor_thread.start()

        # Unknown Controller
        else:
            print('Unknown Controller')
            pass

    # Read Controller values
    # ------------------------------
    def read(self):

        # buttonA = self.Button.DPad_Left
        # buttonB = self.Button.DPad_Right
        # buttonX = self.Button.DPad_Down
        # buttonY = self.Button.DPad_Up

        # joyLeft = ControllerToolbox._Joystick(self.Axis.JoystickLeft_X, self.Axis.JoystickLeft_Y)
        # joyRight = ControllerToolbox._Joystick(self.Axis.JoystickRight_X, self.Axis.JoystickRight_Y)

        # trigger = ControllerToolbox._Trigger(self.Axis.TriggerLeft, self.Axis.TriggerRight)

        # return [self.Axis.JoystickLeft_X, joyLeft.X, self.Axis.JoystickLeft_Y, joyLeft.Y, trigger.L, trigger.R]

        joyLeftX_DB = ControllerToolbox.calcMinMaxScaling_DB(self.Axis.JoyL_X,
                                                          -32768,
                                                          32767,
                                                          5000,
                                                          -100.0,
                                                          100.0)

        joyLeftX = ControllerToolbox.calcMinMaxScaling(self.Axis.JoyL_X,
                                                          -32768,
                                                          32767,
                                                          -100.0,
                                                          100.0)

        return[self.Axis.JoyL_X, joyLeftX_DB, joyLeftX]

    # XBOX Controller Monitor
    # ------------------------------    
    def _XBOX_ControllerMonitor(self):
        
        # While-Loop for detecting controller inputs
        while(True):
            
            # Get Controller Action from reading Gamepad object
            events = self.gamepad.read()

            # Loop through all event in events
            for event in events:
                
                # Axis Event
                # Get incomming Axis-Input from Controller (integer values)
                ControllerToolbox.XBOX_AxisEvent(event, ControllerToolbox._CONST_XBOXONE, self.Axis)

                # Button Event
                # Get incomming Button-Input from Controller (bool values)
                ControllerToolbox.XBOX_ButtonEvent(event, ControllerToolbox._CONST_XBOXONE, self.Button)

    # Playstation 3 Controller Monitor
    # ------------------------------    
    def _PS3_ControllerMonitor(self):
        
        # While-Loop for detecting controller inputs
        while True:
            
            # Get Controller Action
            events = self.gamepad.read()

            # Loop through all event in events
            for event in events:

                # Axis Event
                # Get incomming Axis-Input from Controller (integer values)
                ControllerToolbox.PS3_AxisEvent(event, ControllerToolbox._CONST_PS3, self.Axis)

                # Button Event
                # Get incomming Button-Input from Controller (bool values)
                ControllerToolbox.PS3_ButtonEvent(event, ControllerToolbox._CONST_PS3, self.Button)

# Main Function
# ------------------------------   
if __name__ == '__main__':

    xbox_controller = Controller()

    while True:
        print(xbox_controller.read())
        