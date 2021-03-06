# Controller
# ------------------------------
# Description:
# Read input values from external gamepad Controller

# Version
# ------------------------------
# 0.0   -   Initial version
#           [20.06.2022] - Jan T. Olsen

# Import packages
import threading
import time

# Import Toolbox
import ctrl_toolbox as CtrlToolbox

# Import Class Files
from lib.joystick import Joystick
from lib.trigger import Trigger
from lib.dpad import DPad
from lib.button import XboxButton
from lib.button import PSButton

# Controller Class
# ------------------------------
class Controller():

    # Class constructor
    # ------------------------------
    def __init__(self):

        # Define Controller Members
        # (based on Dataclasses from Controller-Toolbox)
        self.GenericAxis = CtrlToolbox.GenericAxisData()
        self.GenericButton = CtrlToolbox.GenericButtonData()

        # Constants
        self.XBOX_CONST = CtrlToolbox.XBOXONE_CONST()
        self.PS3_CONST = CtrlToolbox.PS3_CONST()
        
        # Search for connected controller
        # (using CtrlToolbox. function)
        self.gamepad = CtrlToolbox.get_controller()
        
        # Determine the type of Controller
        # (using CtrlToolbox. function)
        self.gamepad_type = CtrlToolbox.get_controller_type(self.gamepad)

        # Controller Initialized
        self.init = False

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

            # Controller Initialization done
            self.init = True

        # Playstation 3 Controller
        elif self.gamepad_type == 'PS3':

            # Define Controller Classes
            self.JoyLeft = Joystick('JOY_L', self.PS3_CONST)
            self.JoyRight = Joystick('JOY_R', self.PS3_CONST)
            self.TrigLeft = Trigger('L' ,self.XBOX_CONST)
            self.TrigRight = Trigger('R' ,self.XBOX_CONST)
            self.Button = PSButton()
            self.DPad = DPad()

            # Configure thread
            self._monitor_thread = threading.Thread(target=self._PS3_ControllerMonitor, args=())
            self._monitor_thread.daemon = True

            # Start PS3-Controller-Monitor
            self._monitor_thread.start()

            # Controller Initialization done
            self.init = True

        # Unknown Controller
        else:
            # Controller Initialization failed
            self.init = False

            # Raise Error 
            raise TypeError('Unknown Controller')

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
                CtrlToolbox.XBOX_event_Axis(event,
                                        self.XBOX_CONST,
                                        self.JoyLeft.joystickData,
                                        self.JoyRight.joystickData,
                                        self.TrigLeft.triggerData,
                                        self.TrigRight.triggerData,
                                        self.GenericAxis)

                # Button Event
                # Get incomming Button-Input from Controller (bool values)
                CtrlToolbox.XBOX_event_Button(event,
                                          self.XBOX_CONST,
                                          self.JoyLeft.joystickData,
                                          self.JoyRight.joystickData,
                                          self.TrigLeft.triggerData,
                                          self.TrigRight.triggerData,
                                          self.DPad.dPadData,
                                          self.Button.xboxButtonData,
                                          self.GenericButton)

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
                CtrlToolbox.PS3_event_Axis(event,
                                       self.PS3_CONST,
                                       self.JoyLeft.joystickData,
                                       self.JoyRight.joystickData,
                                       self.TrigLeft.triggerData,
                                       self.TrigRight.triggerData,
                                       self.GenericAxis)

                # Button Event
                # Get incomming Button-Input from Controller (bool values)
                CtrlToolbox.PS3_event_Button(event,
                                         self.PS3_CONST,
                                         self.JoyLeft.joystickData,
                                         self.JoyRight.joystickData,
                                         self.TrigLeft.triggerData,
                                         self.TrigRight.triggerData,
                                         self.DPad.dPadData,
                                         self.Button.psButtonData,
                                         self.GenericButton)

# Main Function
# ------------------------------   
if __name__ == '__main__':

    xboxController = Controller()

    while xboxController.init:
        
        xboxController.update()

        print('Xbox Controller:')
        # print(xbox_controller.JoyLeft.getJoystick())
        # print(xbox_controller.JoyRight.getJoystick())

        # print(xbox_controller.TrigLeft.getTrigger())
        # print(xbox_controller.TrigRight.getTrigger())
        
        print(xboxController.DPad.get_DPad())
        print(xboxController.Button.get_buttons())
        print('\n')

        time.sleep(0.100)

        