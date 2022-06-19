# XBOX Controller
# ------------------------------
# Description:
# Enabling interacting with XBOX Controller
# reading input values from the controller

# Version
# ------------------------------
# 0.0   -   Initial version
#           [19.06.2022] - Jan T. Olsen

# Import packages
from inputs import get_gamepad
import struct
import threading
import enum

# Constants
# ------------------------------
# Defining Axis constants
# class AXIS_KEY(enum.Enum):
AXIS_KEY = 'Absolute'       # Axis Event
JL_X = 'ABS_X'              # Joystick Left - Axis X
JL_Y = 'ABS_Y'              # Joystick Left - Axis Y
JR_X = 'ABS_RX'             # Joystick Right - Axis X
JR_Y = 'ABS_RY'             # Joystick Right - Axis Y
TL = 'ABS_Z'                # Trigger Left - Axis
TR = 'ABS_RZ'               # Trigger Right - Axis

# Defining Button constants
# class BUTTON_KEY(enum.Enum):
BTN_KEY = 'Key'             # Button Event
DX = 'ABS_HAT0X'            # D-Pad - Axis X
DY = 'ABS_HAT0Y'            # D-Pad - Axis Y
BTN_A = 'BTN_SOUTH'         # Button - A
BTN_B = 'BTN_EAST'          # Button - B
BTN_X = 'BTN_WEST'          # Button - X
BTN_Y = 'BTN_NORTH'         # Button - Y
BTN_LB = 'BTN_TL'           # Button - Left-Back
BTN_RB = 'BTN_TR'           # Button - Right-Back   
BTN_JL = 'BTN_THUMBL'       # Button - Joystick Left Push
BTN_JR = 'BTN_THUMBR'       # Button - Joystick Right Push
BTN_START = 'BTN_START'     # Button - Start
BTN_SELECT = 'BTN_SELECT'   # Button - Start


    
# XBOX Controller Class
# ------------------------------
class XboxController():

    # Class constructor
    # ------------------------------
    def __init__(self):

        # Initialize Axis
        self.Axis_JoyLeft_X = 0     # Joystick Left - Axis X
        self.Axis_JoyLeft_Y = 0     # Joystick Left - Axis Y
        self.Axis_JoyRight_X = 0    # Joystick Right - Axis 
        self.Axis_JoyRight_Y = 0    # Joystick Right - Axis 
        self.Axis_TrigLeft = 0      # Trigger Left - Axis
        self.Axis_TrigRight = 0     # Trigger Right - Axis

        # Initialize Buttons
        self.DPad_Left = 0          # D-Pad - Left
        self.DPad_Right = 0         # D-Pad - Right
        self.DPad_Up = 0            # D-Pad - Up
        self.DPad_Down = 0          # D-Pad - Down
        self.Button_A = 0           # Button - A
        self.Button_B = 0           # Button - B
        self.Button_X = 0           # Button - X
        self.Button_Y = 0           # Button - Y
        self.Button_LB = 0          # Button - Left-Back
        self.Button_RB = 0          # Button - Right-Back
        self.Button_JoyLeft_PB = 0  # Button - Joystick Left Push
        self.Button_JoyRight_PB = 0 # Button - Joystick Right Push
        self.Button_Start = 0       # Button - Start
        self.Button_Select = 0      # Button - Select

        # Initialize Controller Monitor on a designated thread
        # ------------------------------
        self._monitor_thread = threading.Thread(target=self.controller_monitor, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    # Read Controller values
    # ------------------------------
    def read(self):
        joyLeftX = self.Axis_JoyLeft_X
        joyLeftY = self.Axis_JoyLeft_Y
        joyRightX = self.Axis_JoyRight_X
        joyRightY = self.Axis_JoyRight_Y

        buttonA = self.Button_A
        buttonB = self.Button_B

        return [joyLeftX, joyLeftY, buttonA, buttonB, joyRightX, joyRightY]
        
    # Controller Monitor
    # # ------------------------------    
    def controller_monitor(self):

        # While-Loop for detecting controller inputs
        while True:

            # Get Controller Action
            events = get_gamepad()

            # Loop through all event in events
            for event in events:

                # Axis Event
                # ------------------------------
                # Incomming Controller-Input are Axis-Values (integer values)
                if event.ev_type == AXIS_KEY:

                    if event.code == JL_X:
                        self.Axis_JoyLeft_X = event.state

                    elif event.code == JL_Y:
                        self.Axis_JoyLeft_Y = event.state

                    elif event.code == JR_X:
                        self.Axis_JoyRight_X = event.state

                    elif event.code == JR_Y:
                        self.Axis_JoyRight_Y = event.state

                # Button Event
                # ------------------------------
                # Incomming Controller-Input are Button-values (boolean values)
                elif event.ev_type == BTN_KEY:

                    if event.code == BTN_A:
                        self.Button_A = event.state

                    elif event.code == BTN_B:
                        self.Button_B = event.state

def test(self, event):

    if event.code == BTN_A:
        self.Button_A = event.state

    elif event.code == BTN_B:
        self.Button_B = event.state

if __name__ == '__main__':

    xbox_controller = XboxController()
    while True:
        print(xbox_controller.read())

       

        
     


    

