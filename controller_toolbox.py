# Controller Toolbox
# ------------------------------
# Description:
# Toolbox for utility classes and methods
# to be used with an external controller

# Version
# ------------------------------
# 0.0   -   Initial version
#           [20.06.2022] - Jan T. Olsen

# Import packages
from dataclasses import dataclass
from inputs import devices
from logging import NullHandler

# Dataclass - Axis 
# ------------------------------
# Member related to Controller Axis
@dataclass
class _Axis:
    
    # Declare Axis members
    JoystickLeft_X : float = 0.0        # Joystick Left - Axis X
    JoystickLeft_Y : float = 0.0        # Joystick Left - Axis Y
    JoystickRight_X : float = 0.0       # Joystick Right - Axis X
    JoystickRight_Y : float = 0.0       # Joystick Right - Axis Y
    TriggerLeft : float = 0.0           # Trigger Left - Axis
    TriggerRight : float = 0.0          # Trigger Left - Axis

# Dataclass - Buttons 
# ------------------------------
# Members related to Controller Buttons
@dataclass
class _Button:
    
    # Declare Button members
    A : bool = False            # Button - A
    B : bool = False            # Button - B
    X : bool = False            # Button - X
    Y : bool = False            # Button - Y
    LB: bool = False            # Button - Left-Back
    RB: bool = False            # Button - Right-Back
    Start : bool = False        # Button - Start
    Select : bool = False       # Button - Select

    PB_Left : bool = False      # Joystick Left - Pushbutton
    PB_Right : bool = False     # Joystick Right - Pushbutton

    DPad_Left : bool = False    # D-Pad - Left
    DPad_Right : bool = False   # D-Pad - Right
    DPad_Up : bool = False      # D-Pad - Up
    DPad_Down : bool = False    # D-Pad - Down

# Dataclass - XBOX One Constants
# ------------------------------
@dataclass
class _CONST_XBOXONE:
    
    # Defining Axis constants
    AXIS_KEY = 'Absolute'       # Axis Event
    JL_X = 'ABS_X'              # Joystick Left - Axis X
    JL_Y = 'ABS_Y'              # Joystick Left - Axis Y
    JR_X = 'ABS_RX'             # Joystick Right - Axis X
    JR_Y = 'ABS_RY'             # Joystick Right - Axis Y
    TL = 'ABS_Z'                # Trigger Left - Axis
    TR = 'ABS_RZ'               # Trigger Right - Axis

    # Defining Button constants
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

# Dataclass - PS3 Constants
# ------------------------------
@dataclass
class _CONST_PS3:
    
    # Defining Axis constants
    AXIS_EVENT = 'Absolute'     # Axis Event
    JL_X = 'ABS_X'              # Joystick Left - Axis X
    JL_Y = 'ABS_Y'              # Joystick Left - Axis Y
    JR_X = 'ABS_RX'             # Joystick Right - Axis X
    JR_Y = 'ABS_RY'             # Joystick Right - Axis Y
    TL = 'ABS_Z'                # Trigger Left - Axis
    TR = 'ABS_RZ'               # Trigger Right - Axis

    # Defining Button constants
    BTN_EVENT = 'Key'           # Button Event
    DPAD_L = 'BTN_DPAD_LEFT'    # D-Pad - Left
    DPAD_R = 'BTN_DPAD_RIGHT'   # D-Pad - Right
    DPAD_U = 'BTN_DPAD_UP'      # D-Pad - Up
    DPAD_D = 'BTN_DPAD_DOWN'    # D-Pad - Down
    BTN_A = 'BTN_SOUTH'         # Button - A
    BTN_B = 'BTN_EAST'          # Button - B
    BTN_X = 'BTN_WEST'          # Button - X
    BTN_Y = 'BTN_NORTH'         # Button - Y
    BTN_LB = 'BTN_TL'           # Button - Left-Back
    BTN_RB = 'BTN_TR'           # Button - Right-Back  
    BTN_LB2 = 'BTN_TL2'         # Button - Left-Back Trigger
    BTN_RB2 = 'BTN_TR2'         # Button - Right-Back Trigger      
    BTN_PBL = 'BTN_THUMBL'      # Button - Joystick Left Push
    BTN_PBR = 'BTN_THUMBR'      # Button - Joystick Right Push
    BTN_START = 'BTN_START'     # Button - Start
    BTN_SELECT = 'BTN_SELECT'   # Button - Start

# Get Connected Controller
# -----------------------------
def getController():
    # Using the first valid gamepad
    try:
        gamepad = devices.gamepads[0]
    except IndexError:
        print ('No gamepad found!')
        return NullHandler
    return gamepad

# Get Controller Type
# -----------------------------
def getControllerType():

    # Get Connected Controller
    gamepad = getController()

    # Convert type to string 
    gamepad_typename = format(gamepad)

    # Determine type
    # (search for keyword within Gamepad typename)
    if 'Microsoft' in gamepad_typename:
        # XBOX Controller
        gamepad_type = 'XBOX'
    
    elif 'PLAYSTATION(R)3' in gamepad_typename:
        # Playstation 3 Controller
        gamepad_type = 'PS3'

    else:
        # Unknown Controller
        gamepad_type = 'UNKNOWN'

    # Return Controller Type
    return gamepad_type

    