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

# Controller Class
# ------------------------------
class Controller():

    # Class constructor
    # ------------------------------
    def __init__(self):

        # Define Controller Members
        # (based on Dataclasses from Controller-Toolbox)
        self.Axis = ControllerToolbox._Axis()
        self.Button = ControllerToolbox._Button()

        # Search for connected controller
        # (using ControllerToolbox function)
        self.gamepad = ControllerToolbox.getController()

        # Determine the type of Controller
        # (using ControllerToolbox function)
        self.gamepad_type = ControllerToolbox.getControllerType()

        # Initialize Controller Monitor on a designated thread
        # ------------------------------
        # Based on the Controller-Type launch the related controller-monitor-thread

        # XBOX Controller
        if self.gamepad_type == 'XBOX':
            # Configure thread
            self._monitor_thread = threading.Thread(target=self._XBOX_Controller_monitor, args=())
            self._monitor_thread.daemon = True

            # Start XBOX-Controller-Monitor
            self._monitor_thread.start()

        # Playstation 3 Controller
        elif self.gamepad_type == 'PS3':
            # Configure thread
            self._monitor_thread = threading.Thread(target=self._PS3_Controller_monitor, args=())
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

        joyLeftX = self.Axis.JoystickLeft_X
        joyLeftY = self.Axis.JoystickLeft_Y

        return [joyLeftX, joyLeftY]

    # XBOX Controller Monitor
    # ------------------------------    
    def _XBOX_Controller_monitor(self):
        
        # While-Loop for detecting controller inputs
        while True:
            
            # Get Controller Action
            events = self.gamepad.read()

            # Loop through all event in events
            for event in events:

                # Axis Event
                # ------------------------------
                # Incomming Controller-Input are Axis-Values (integer values)
                if event.ev_type == ControllerToolbox._CONST_XBOXONE.AXIS_KEY:
                    
                    if event.code == ControllerToolbox._CONST_XBOXONE.JL_X:
                        self.Axis.JoystickLeft_X = event.state

                    elif event.code == ControllerToolbox._CONST_XBOXONE.JL_Y:
                        self.Axis.JoystickLeft_Y = event.state

    # Playstation 3 Controller Monitor
    # ------------------------------    
    def _PS3_Controller_monitor(self):
        print(self.gamepad_type)

   

if __name__ == '__main__':

    xbox_controller = Controller()

    while True:
        print(xbox_controller.read())
        