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
    A : bool = 0            # Button - A
    B : bool = 0            # Button - B
    X : bool = 0            # Button - X
    Y : bool = 0            # Button - Y
    LB: bool = 0            # Button - Left-Back
    RB: bool = 0            # Button - Right-Back
    Start : bool = 0        # Button - Start
    Select : bool = 0       # Button - Select

    PB_Left : bool = 0      # Joystick Left - Pushbutton
    PB_Right : bool = 0     # Joystick Right - Pushbutton

    DPad_Left : bool = 0    # D-Pad - Left
    DPad_Right : bool = 0   # D-Pad - Right
    DPad_Up : bool = 0      # D-Pad - Up
    DPad_Down : bool = 0    # D-Pad - Down

    LB2: bool = 0           # Button - Left-Back Trigger
    RB2: bool = 0           # Button - Right-Back Trigger
    
# Dataclass - XBOX One Constants
# ------------------------------
@dataclass
class _CONST_XBOXONE:
    
    # Defining Axis constants
    AXIS_EVENT = 'Absolute'     # Axis Event
    JOYL_X = 'ABS_X'            # Joystick Left - Axis X
    JOYL_Y = 'ABS_Y'            # Joystick Left - Axis Y
    JOYR_X = 'ABS_RX'           # Joystick Right - Axis X
    JOYR_Y = 'ABS_RY'           # Joystick Right - Axis Y
    TRG_L = 'ABS_Z'             # Trigger Left - Axis
    TRG_R = 'ABS_RZ'            # Trigger Right - Axis

    # Defining Button constants
    BTN_EVENT = 'Key'           # Button Event
    DPAD_X = 'ABS_HAT0X'        # D-Pad - Axis X
    DPAD_Y = 'ABS_HAT0Y'        # D-Pad - Axis Y
    BTN_A = 'BTN_SOUTH'         # Button - A
    BTN_B = 'BTN_EAST'          # Button - B
    BTN_X = 'BTN_WEST'          # Button - X
    BTN_Y = 'BTN_NORTH'         # Button - Y
    BTN_LB = 'BTN_TL'           # Button - Left-Back
    BTN_RB = 'BTN_TR'           # Button - Right-Back   
    BTN_PBL = 'BTN_THUMBL'      # Button - Joystick Left Push
    BTN_PBR = 'BTN_THUMBR'      # Button - Joystick Right Push
    BTN_START = 'BTN_START'     # Button - Start
    BTN_SELECT = 'BTN_SELECT'   # Button - Select

    # Axis Min / Max Values
    JOY_MIN = -32768
    JOY_MAX = 32767
    JOY_DB = 2500
    TRG_MIN = 0
    TRG_MAX = 255
    TRG_DB = 0

# Dataclass - PS3 Constants
# ------------------------------
@dataclass
class _CONST_PS3:
    
    # Defining Axis constants
    AXIS_EVENT = 'Absolute'     # Axis Event
    JOYL_X = 'ABS_X'            # Joystick Left - Axis X
    JOYL_Y = 'ABS_Y'            # Joystick Left - Axis Y
    JOYR_X = 'ABS_RX'           # Joystick Right - Axis X
    JOYR_Y = 'ABS_RY'           # Joystick Right - Axis Y
    TRG_L = 'ABS_Z'             # Trigger Left - Axis
    TRG_R = 'ABS_RZ'            # Trigger Right - Axis

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
    BTN_SELECT = 'BTN_SELECT'   # Button - Select

# Dataclass - Joystick 
# ------------------------------
# Member related to Controller Joystick
@dataclass
class _Joystick():
    """
    Joystick Object
    Scales the raw Axis-Value obtained from Controller-Input
    and compensates for Deadband

    :param raw_X: Joystick X-Axis raw value
    :param raw_Y: Joystick Y-Axis raw value
    :param raw_min: Axis Raw Minimum value
    :param raw_max: Axis Raw Maximum value
    :param raw_db: Axis Raw deadband value
    :param eu_min: Engineering Unit Minimum value
    :param eu_max: Engineering Unit Maximum value
    :return X: Joystick X-Axis Value (float)
    :return Y: Joystick X-Axis Value (float)
    """

    def __init__(self, 
                raw_X : int, 
                raw_Y : int,
                raw_min : int = _CONST_XBOXONE.JOY_MIN, 
                raw_max : int = _CONST_XBOXONE.JOY_MAX,
                raw_db : int = _CONST_XBOXONE.JOY_DB,
                eu_min : float = -100.0 , 
                eu_max : float = 100.0,):

        # Deadband - Joystick X
        if abs(raw_X) < abs(raw_db):
            raw_X = 0

        # Deadband - Joystick Y
        if abs(raw_Y) < abs(raw_db):
            raw_Y = 0

        # Scale Axis Input
        self.X = scaleAxisInput(raw_X, raw_min, raw_max, eu_min, eu_max)
        self.Y = scaleAxisInput(raw_Y, raw_min, raw_max, eu_min, eu_max)

# Dataclass - Trigger 
# ------------------------------
# Member related to Controller Trigger
@dataclass
class _Trigger():
    """
    Trigger Object
    Scales the raw Axis-Value obtained from Controller-Input
    and compensates for deadband
    
    :param raw_L: Trigger Right raw value
    :param raw_R: Trigger Right raw value
    :param raw_min: Axis Raw Minimum value
    :param raw_max: Axis Raw Maximum value
    :param raw_db: Axis Raw deadband value
    :param eu_min: Engineering Unit Minimum value
    :param eu_max: Engineering Unit Maximum value
    :return L: Trigger Left Value (float)
    :return R: Trigger Right Value (float)
    """
    
    def __init__(self, 
                raw_L : int, 
                raw_R : int,
                raw_min : int = _CONST_XBOXONE.TRG_MIN, 
                raw_max : int = _CONST_XBOXONE.TRG_MAX,
                raw_db : int = _CONST_XBOXONE.TRG_DB,
                eu_min : float = 0.0 , 
                eu_max : float = 100.0,):

        # Deadband - Trigger Left
        if abs(raw_L) < abs(raw_db):
            raw_L = 0

        # Deadband - Trigger Right
        if abs(raw_R) < abs(raw_db):
            raw_R = 0

        # Scale Axis Input
        self.L = scaleAxisInput(raw_L, raw_min, raw_max, eu_min, eu_max)
        self.R = scaleAxisInput(raw_R, raw_min, raw_max, eu_min, eu_max)


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

# Scale Axis Input Value
# -----------------------------
def scaleAxisInput(raw_value : int, 
                    raw_min : int, 
                    raw_max : int,
                    eu_min : float, 
                    eu_max : float):
    """
    Scale Axis Input 
    Scale the raw Axis-Value obtained from Controller-Input
    :param raw_value: Axis raw value
    :param raw_min: Axis Raw Minimum value
    :param raw_max: Axis Raw Maximum value
    :param eu_min: Engineering Unit Minimum value
    :param eu_max: Engineering Unit Maximum value
    :return value: Scaled Axis Value (float)
    """
    # Scaling input-value to range: [0 , 1]
    tmp_value = (raw_value - raw_min) / (raw_max - raw_min)

    # Scaling input-value to range: [min , max]
    value = tmp_value * (eu_max - eu_min) + eu_min

    # Function return
    return value

# XBOX Controller - Axis Event
# ------------------------------
def XBOX_AxisEvent(event : any, 
                   CONST_XBOXONE : _CONST_XBOXONE, 
                   Axis : _Axis):
    """
    XBOX Controller
    Get incomming Axis-Events from Controller-Input (integer values)
    :param event: Element of Events from Connected Gamepad object
    :param CONST_XBOXONE: XBOX Controller Constants
    :return param Axis: Axis-Dataclass (_AXIS)
    """

    # Axis Event
    # Incomming Axis-Input from Controller (integer values)
    if event.ev_type == CONST_XBOXONE.AXIS_EVENT:
        
        # Joystick Left - Axis X
        if event.code == CONST_XBOXONE.JOYL_X:
            Axis.JoystickLeft_X = event.state

        # Joystick Left - Axis Y
        elif event.code == CONST_XBOXONE.JOYL_Y:
            Axis.JoystickLeft_Y = event.state

        # Joystick Right - Axis X
        elif event.code == CONST_XBOXONE.JOYR_X:
            Axis.JoystickRight_X = event.state

        # Joystick Right - Axis Y
        elif event.code == CONST_XBOXONE.JOYR_Y:
            Axis.JoystickRight_Y = event.state

        # Trigger Left - Axis
        elif event.code == CONST_XBOXONE.TRG_L:
            Axis.TriggerLeft = event.state

        # Trigger Right - Axis
        elif event.code == CONST_XBOXONE.TRG_R:
            Axis.TriggerRight = event.state

    # Function return
    return Axis

# XBOX Controller - Button Event
# ------------------------------
def XBOX_ButtonEvent(event : any, 
                     CONST_XBOXONE : _CONST_XBOXONE, 
                     Button : _Button):
    """
    XBOX Controller
    Get incomming Button-Events from Controller-Input (bool values)
    :param event: Element of Events from Connected Gamepad object
    :param CONST_XBOXONE: XBOX Controller Constants
    :return param Button: Button-Dataclass (_Button)
    """

    # Button Event
    # Incomming Button-Input from Controller (bool values)
    if event.ev_type == CONST_XBOXONE.BTN_EVENT:
        
        # Button - A
        if event.code == CONST_XBOXONE.BTN_A:
            Button.A = event.state

        # Button - B
        elif event.code == CONST_XBOXONE.BTN_B:
            Button.B = event.state

        # Button - X
        elif event.code == CONST_XBOXONE.BTN_X:
            Button.X = event.state

        # Button - Y
        elif event.code == CONST_XBOXONE.BTN_Y:
            Button.Y = event.state

        # Button - Left-Back
        elif event.code == CONST_XBOXONE.BTN_LB:
            Button.LB = event.state

        # Button - Right-Back
        elif event.code == CONST_XBOXONE.BTN_RB:
            Button.RB = event.state

        # Button - Joystick Left Push
        elif event.code == CONST_XBOXONE.BTN_PBL:
            Button.PB_Left = event.state

        # Button - Joystick Right Push
        elif event.code == CONST_XBOXONE.BTN_PBR:
            Button.PB_Right = event.state

        # Button - Start
        elif event.code == CONST_XBOXONE.BTN_START:
            Button.Start = event.state

        # Button - Select
        elif event.code == CONST_XBOXONE.BTN_SELECT:
            Button.Select = event.state

    # Axis Event
    # Special case for D-PAD and Trigger buttons
    if event.ev_type == CONST_XBOXONE.AXIS_EVENT:

        # D-PAD - Left / Right
        if event.code == CONST_XBOXONE.DPAD_X:
            
            # Determine Left/Right by sign of state-value
            if event.state < 0:
                Button.DPad_Left = 1

            elif event.state > 0:
                Button.DPad_Right = 1

            # Reset D-PAD - Left / Right values
            else:
                Button.DPad_Left = 0
                Button.DPad_Right = 0
            
        # D-PAD - Up / Down
        elif event.code == CONST_XBOXONE.DPAD_Y:

            # Determine Up/Down by sign of state-value
            if event.state < 0:
                Button.DPad_Up = 1

            elif event.state > 0:
                Button.DPad_Down = 1

            # Reset D-PAD - Up / Down values
            else:
                Button.DPad_Up = 0
                Button.DPad_Down = 0

        # Button - Left-Back Trigger
        elif event.code == CONST_XBOXONE.TRG_L:

            # Determine if active
            if event.state > 0:
                Button.LB2 = 1

            # Reset Left-Back Trigger
            else:
                Button.LB2 = 0

        # Button - Right-Back Trigger
        elif event.code == CONST_XBOXONE.TRG_R:

            # Determine if active
            if event.state > 0:
                Button.RB2 = 1

            # Reset Left-Back Trigger
            else:
                Button.RB2 = 0

    # Function return
    return Button

# PS3 Controller - Axis Event
# ------------------------------
def PS3_AxisEvent(event : any, 
                   CONST_PS3 : _CONST_PS3, 
                   Axis : _Axis):
    """
    PS3 Controller
    Get incomming Axis-Events from Controller-Input (integer values)
    :param event: Element of Events from Connected Gamepad object
    :param CONST_PS3: PS3 Controller Constants
    :return param Axis: Axis-Dataclass (_AXIS)
    """

    # Axis Event
    # Incomming Axis-Input from Controller (integer values)
    if event.ev_type == CONST_PS3.AXIS_EVENT:
        
        # Joystick Left - Axis X
        if event.code == CONST_PS3.JOYL_X:
            Axis.JoystickLeft_X = event.state

        # Joystick Left - Axis Y
        elif event.code == CONST_PS3.JOYL_Y:
            Axis.JoystickLeft_Y = event.state

        # Joystick Right - Axis X
        elif event.code == CONST_PS3.JOYR_X:
            Axis.JoystickRight_X = event.state

        # Joystick Right - Axis Y
        elif event.code == CONST_PS3.JOYR_Y:
            Axis.JoystickRight_Y = event.state

        # Trigger Left - Axis
        elif event.code == CONST_PS3.TRG_L:
            Axis.TriggerLeft = event.state

        # Trigger Right - Axis
        elif event.code == CONST_PS3.TRG_R:
            Axis.TriggerRight = event.state

    # Function return
    return Axis

# PS3 Controller - Button Event
# ------------------------------
def PS3_ButtonEvent(event : any, 
                     CONST_PS3 : _CONST_PS3, 
                     Button : _Button):
    """
    PS3 Controller
    Get incomming Button-Events from Controller-Input (bool values)
    :param event: Element of Events from Connected Gamepad object
    :param CONST_PS3: PS3 Controller Constants
    :return param Button: Button-Dataclass (_Button)
    """

    # Button Event
    # Incomming Button-Input from Controller (bool values)
    if event.ev_type == CONST_PS3.BTN_EVENT:
        
        # Button - A
        if event.code == CONST_PS3.BTN_A:
            Button.A = event.state

        # Button - B
        elif event.code == CONST_PS3.BTN_B:
            Button.B = event.state

        # Button - X
        elif event.code == CONST_PS3.BTN_X:
            Button.X = event.state

        # Button - Y
        elif event.code == CONST_PS3.BTN_Y:
            Button.Y = event.state

        # Button - Left-Back
        elif event.code == CONST_PS3.BTN_LB:
            Button.LB = event.state

        # Button - Right-Back
        elif event.code == CONST_PS3.BTN_RB:
            Button.RB = event.state

        # Button - Joystick Left Push
        elif event.code == CONST_PS3.BTN_PBL:
            Button.PB_Left = event.state

        # Button - Joystick Right Push
        elif event.code == CONST_PS3.BTN_PBR:
            Button.PB_Right = event.state

        # Button - Start
        elif event.code == CONST_PS3.BTN_START:
            Button.Start = event.state

        # Button - Select
        elif event.code == CONST_PS3.BTN_SELECT:
            Button.Select = event.state

        # D-PAD - Left
        if event.code == CONST_PS3.DPAD_L:
            Button.DPad_Left = event.state

        # D-PAD - Right
        elif event.code == CONST_PS3.DPAD_R:
            Button.DPad_Right = event.state

        # D-PAD - Up
        elif event.code == CONST_PS3.DPAD_U:
            Button.DPad_Down = event.state

        # D-PAD - Down
        elif event.code == CONST_PS3.DPAD_D:
            Button.DPad_Down = event.state

        # Button - Left-Back Trigger
        elif event.code == CONST_PS3.BTN_LB2:
            Button.LB2 = event.state

        # Button - Right-Back Trigger
        elif event.code == CONST_PS3.BTN_RB2:
            Button.RB2 = event.state

    # Function return
    return Button
    