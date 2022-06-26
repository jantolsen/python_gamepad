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

# Import Class-Files and Toolbox
import controller_toolbox as ControllerToolbox

# Import Class Files
from controller_joystick import Joystick as Joystick
from controller_trigger import Trigger as Trigger
from controller_dpad import DPad as DPad
from controller_button import XboxButton as XboxButton
from controller_button import PSButton as PSButton

# Controller Class
# ------------------------------
class Controller():

    # Class constructor
    # ------------------------------
    def __init__(self):

        # Define Controller Members
        # (based on Dataclasses from Controller-Toolbox)
        self.GenericAxis = ControllerToolbox.GenericAxisData()
        self.GenericButton = ControllerToolbox.GenericButtonData()

        # Constants
        self.XBOX_CONST = ControllerToolbox.XBOXONE_CONST()
        self.PS3_CONST = ControllerToolbox.PS3_CONST()
        
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
            
            # Define Controller Classes
            self.JoyLeft = Joystick('JOY_L', self.XBOX_CONST)
            self.JoyRight = Joystick('JOY_R', self.XBOX_CONST)
            self.TrigLeft = Trigger('L' ,self.XBOX_CONST)
            self.TrigRight = Trigger('R' ,self.XBOX_CONST)
            self.Button = XboxButton()
            self.DPad = DPad()

            # Configure thread
            self._monitor_thread = threading.Thread(target=self._XBOX_ControllerMonitor, args=())
            self._monitor_thread.daemon = True

            # Start XBOX-Controller-Monitor
            self._monitor_thread.start()

        # Playstation 3 Controller
        elif self.gamepad_type == 'PS3':

            # Define Controller Classes
            self.JoyLeft = Joystick('JOY_L', self.PS3_CONST)
            self.JoyRight = Joystick('JOY_R', self.PS3_CONST)
            self.TrigLeft = Trigger(self.PS3_CONST)
            self.TrigRight = Trigger(self.PS3_CONST)
            self.Button = PSButton()
            self.DPad = DPad()

            # Configure thread
            self._monitor_thread = threading.Thread(target=self._PS3_ControllerMonitor, args=())
            self._monitor_thread.daemon = True

            # Start PS3-Controller-Monitor
            self._monitor_thread.start()

        # Unknown Controller
        else:
            print('Unknown Controller')
            pass

    # Update Controller values
    # ------------------------------
    def update(self):

        # Joystick Update
        self.JoyLeft.update()
        self.JoyRight.update()

        # Trigger Update
        self.TrigLeft.update()
        self.TrigRight.update()

        # Button update
        self.DPad.update()
        self.Button.update()
        
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
                ControllerToolbox.XBOX_AxisEvent(event,
                                                self.XBOX_CONST,
                                                self.JoyLeft.joystickData,
                                                self.JoyRight.joystickData,
                                                self.TrigLeft.triggerData,
                                                self.TrigRight.triggerData,
                                                self.GenericAxis)

                # Button Event
                # Get incomming Button-Input from Controller (bool values)
                ControllerToolbox.XBOX_ButtonEvent(event,
                                                self.XBOX_CONST,
                                                self.JoyLeft.joystickData,
                                                self.JoyRight.joystickData,
                                                self.TrigLeft.triggerData,
                                                self.TrigRight.triggerData,
                                                self.DPad.dPadData,
                                                self.Button.xboxButtonData,
                                                self.GenericAxis)

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
                ControllerToolbox.PS3_AxisEvent(event,
                                                self.PS3_CONST,
                                                self.JoyLeft.joystickData,
                                                self.JoyRight.joystickData,
                                                self.TrigLeft.triggerData,
                                                self.TrigRight.triggerData,
                                                self.GenericAxis)

                # Button Event
                # Get incomming Button-Input from Controller (bool values)
                ControllerToolbox.PS3_ButtonEvent(event,
                                                self.PS3_CONST,
                                                self.JoyLeft.joystickData,
                                                self.JoyRight.joystickData,
                                                self.TrigLeft.triggerData,
                                                self.TrigRight.triggerData,
                                                self.DPad.dPadData,
                                                self.Button.psButtonData,
                                                self.GenericAxis)

# Main Function
# ------------------------------   
if __name__ == '__main__':

    xbox_controller = Controller()

    while True:
        xbox_controller.update()
        

        # print(xbox_controller.DPad.getDPad())
        # print(xbox_controller.Button.getButtons())
        print(xbox_controller.DPad.getDPad())

        