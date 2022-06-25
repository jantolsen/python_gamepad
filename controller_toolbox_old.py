# Controller Toolbox
# ------------------------------
# Description:
# Toolbox for utility classes and methods
# to be used with an external controller

# Version
# ------------------------------
# 0.1   -   Redesign constants dataclasses.
#           Now divided into multiple and nested dataclasses
#           [24.06.2022] - Jan T. Olsen
# 0.0   -   Initial version
#           [20.06.2022] - Jan T. Olsen

# Import packages
from dataclasses import dataclass, field
from inputs import devices
from logging import NullHandler

# Dataclass - Axis 
# ------------------------------
# Member related to Controller Axis
@dataclass
class _AxisData:
    
    # Declare Axis members
    JoyL_X : float = 0.0    # Joystick Left - Axis X
    JoyL_Y : float = 0.0    # Joystick Left - Axis Y
    JoyR_X : float = 0.0    # Joystick Right - Axis X
    JoyR_Y : float = 0.0    # Joystick Right - Axis Y
    Trig_L : float = 0.0     # Trigger Left - Axis
    Trig_R : float = 0.0     # Trigger Left - Axis

# Dataclass - Buttons 
# ------------------------------
# Members related to Controller Buttons
@dataclass
class _ButtonData:
    
    # Declare Button members
    A : bool = 0        # Button - A
    B : bool = 0        # Button - B
    X : bool = 0        # Button - X
    Y : bool = 0        # Button - Y
    LB: bool = 0        # Button - Left-Back
    RB: bool = 0        # Button - Right-Back
    Start : bool = 0    # Button - Start
    Select : bool = 0   # Button - Select

    PB_L : bool = 0     # Joystick Left - Pushbutton
    PB_R : bool = 0     # Joystick Right - Pushbutton

    DPad_L : bool = 0   # D-Pad - Left
    DPad_R : bool = 0   # D-Pad - Right
    DPad_U : bool = 0   # D-Pad - Up
    DPad_D : bool = 0   # D-Pad - Down

    LB2: bool = 0       # Button - Left-Back Trigger
    RB2: bool = 0       # Button - Right-Back Trigger

# Dataclass - Controller Event-Key Constants
# ------------------------------
@dataclass
class _EVENTKEY:
    """
    Controller Event-Key Constants
    Map for each Button and Axis key
    """
    # Axis key constants
    # (No initialization required)
    AXIS_EVENT  : str = field(init=False)   # Axis Event
    JOYL_X      : str = field(init=False)   # Joystick Left - Axis X
    JOYL_Y      : str = field(init=False)   # Joystick Left - Axis Y
    JOYR_X      : str = field(init=False)   # Joystick Right - Axis X
    JOYR_Y      : str = field(init=False)   # Joystick Right - Axis Y
    TRIG_L      : str = field(init=False)   # Trigger Left - Axis
    TRIG_R      : str = field(init=False)   # Trigger Right - Axis

    # Button key constants
    # (No initialization required)
    BTN_EVENT   : str = field(init=False)   # Button Event
    DPAD_X      : str = field(init=False)   # D-Pad - Axis X
    DPAD_Y      : str = field(init=False)   # D-Pad - Axis Y
    DPAD_L      : str = field(init=False)   # D-Pad - Left
    DPAD_R      : str = field(init=False)   # D-Pad - Right
    DPAD_U      : str = field(init=False)   # D-Pad - Up
    DPAD_D      : str = field(init=False)   # D-Pad - Down
    BTN_A       : str = field(init=False)   # Button - A
    BTN_B       : str = field(init=False)   # Button - B
    BTN_X       : str = field(init=False)   # Button - X
    BTN_Y       : str = field(init=False)   # Button - Y
    BTN_LB      : str = field(init=False)   # Button - Left-Back
    BTN_RB      : str = field(init=False)   # Button - Right-Back  
    BTN_LB2     : str = field(init=False)   # Button - Left-Back Trigger
    BTN_RB2     : str = field(init=False)   # Button - Right-Back Trigger  
    BTN_PBL     : str = field(init=False)   # Button - Joystick Left Push
    BTN_PBR     : str = field(init=False)   # Button - Joystick Right Push
    BTN_START   : str = field(init=False)   # Button - Start
    BTN_SELECT  : str = field(init=False)   # Button - Select

# Dataclass - Controller Joystick Scaling Constans
# ------------------------------
@dataclass
class _JOYSCALE():
    """
    Controller Joystick Scaling Constans
    Data constants for scaling Controller Joystick values
    from raw-input values to scaled values
    """
    # Scaling data for Controller Joystick Axis
    # (No initialization required)
    JOY_RAW_MIN : int = field(init=False)        # Joystick Minimum Raw value
    JOY_RAW_MAX : int = field(init=False)        # Joystick Maximum Raw value
    JOY_RAW_DB  : int = field(init=False)        # Joystick Deadband Raw value
    JOY_MIN     : float = field(init=False)      # Joystick Minimum Scaling value
    JOY_MAX     : float = field(init=False)      # Joystick Maximum Scaling value

# Dataclass - Controller Trigger Scaling Constans
# ------------------------------
@dataclass
class _TRIGSCALE():
    """
    Controller Trigger Scaling Constans
    Data constants for scaling Controller Trigger values
    from raw-input values to scaled values
    """
    # Scaling data for Controller Trigger Axis
    # (No initialization required)
    TRIG_RAW_MIN : int = field(init=False)      # Trigger Minimum Raw value
    TRIG_RAW_MAX : int = field(init=False)      # Trigger Maximum Raw value
    TRIG_RAW_DB  : int = field(init=False)      # Trigger Deadband Raw value,
    TRIG_MIN     : float = field(init=False)    # Trigger Minimum Scaling value
    TRIG_MAX     : float = field(init=False)    # Trigger Maximum Scaling value

# Dataclass - Gamepad Controller Constants
# ------------------------------
@dataclass
class _GAMEPAD_CONST:
    """
    Gamepad Controller Constants:
    Dataclass for containing default constants value
    :param (optional)  _EVENTKEY:   Event-Key Constants ()
    :param (optional) _JOYSCALE:   Joystick Scaling Constants
    :param (optional) _TRIGSCALE:  Trigger Scaling Constants
    """
    # XBOX-One Constants
    EVENTKEY    : _EVENTKEY = field(init=False, default_factory = _EVENTKEY)         
    JOYSCALE    : _JOYSCALE = field(init=False, default_factory = _JOYSCALE)
    TRIGSCALE   : _TRIGSCALE = field(init=False, default_factory = _TRIGSCALE)

    def __post_init__(self) -> None:
        # Initialize
        self._INIT_EVENTKEY()
        self._INIT_JOYSCALE()
        self._INIT_TRIGSCALE()
    
    def _INIT_EVENTKEY(self):
        # Defining Axis Event-Key Constants
        self.EVENTKEY.AXIS_EVENT = 'Absolute'   # Axis Event
        self.EVENTKEY.JOYL_X = 'ABS_X'          # Joystick Left - Axis X
        self.EVENTKEY.JOYL_Y = 'ABS_Y'          # Joystick Left - Axis Y
        self.EVENTKEY.JOYR_X = 'ABS_RX'         # Joystick Right - Axis X
        self.EVENTKEY.JOYR_Y = 'ABS_RY'         # Joystick Right - Axis Y
        self.EVENTKEY.TRIG_L = 'ABS_Z'          # Trigger Left - Axis
        self.EVENTKEY.TRIG_R = 'ABS_RZ'         # Trigger Right - Axis

        # Defining Button Event-Key Constants
        self.EVENTKEY.BTN_EVENT = 'Key'         # Button Event
        self.EVENTKEY.DPAD_X = 'ABS_HAT0X'      # D-Pad - Axis X
        self.EVENTKEY.DPAD_Y = 'ABS_HAT0Y'      # D-Pad - Axis Y
        self.EVENTKEY.DPAD_L = 'BTN_DPAD_LEFT'  # D-Pad - Left
        self.EVENTKEY.DPAD_R = 'BTN_DPAD_RIGHT' # D-Pad - Right
        self.EVENTKEY.DPAD_U = 'BTN_DPAD_UP'    # D-Pad - Up
        self.EVENTKEY.DPAD_D = 'BTN_DPAD_DOWN'  # D-Pad - Down
        self.EVENTKEY.BTN_A = 'BTN_SOUTH'       # Button - A
        self.EVENTKEY.BTN_B = 'BTN_EAST'        # Button - B
        self.EVENTKEY.BTN_X = 'BTN_WEST'        # Button - X
        self.EVENTKEY.BTN_Y = 'BTN_NORTH'       # Button - Y
        self.EVENTKEY.BTN_LB = 'BTN_TL'         # Button - Left-Back
        self.EVENTKEY.BTN_RB = 'BTN_TR'         # Button - Right-Back   
        self.EVENTKEY.BTN_LB2 = 'BTN_TL2'       # Button - Left-Back Trigger
        self.EVENTKEY.BTN_RB2 = 'BTN_TR2'       # Button - Right-Back Trigger

    def _INIT_JOYSCALE(self):
        # Defining Joystick Scaling Constants
        self.JOYSCALE.JOY_RAW_MIN = -32768  # Joystick Minimum Raw value
        self.JOYSCALE.JOY_RAW_MAX = 32767   # Joystick Maximum Raw value
        self.JOYSCALE.JOY_RAW_DB = 1000     # Joystick Deadband Raw value
        self.JOYSCALE.JOY_MIN = -100.0      # Joystick Minimum Scaling value
        self.JOYSCALE.JOY_MAX = 100.0       # Joystick Maximum Scaling value

    def _INIT_TRIGSCALE(self):
        # Defining Trigger Scaling Constants
        self.TRIGSCALE.TRIG_RAW_MIN = 0     # Joystick Minimum Raw value
        self.TRIGSCALE.TRIG_RAW_MAX = 255   # Joystick Maximum Raw value
        self.TRIGSCALE.TRIG_RAW_DB = 0      # Joystick Deadband Raw value
        self.TRIGSCALE.TRIG_MIN = 0.0       # Joystick Minimum Scaling value
        self.TRIGSCALE.TRIG_MAX = 100.0     # Joystick Maximum Scaling value

# Dataclass - XBOX One Controller Constants
# ------------------------------
@dataclass
class XBOXONE_CONST(_GAMEPAD_CONST):
    """
    Xbox One - Controller Constants:
    Inherits and uses the default gamepad controller constant dataclass
    and overwrites certain constant values to match the related specific controller type
    """

    def __post_init__(self) -> None:
        # Initialize
        self._INIT_EVENTKEY()
        self._INIT_JOYSCALE()
        self._INIT_TRIGSCALE()
    
    # Overwrite Event-Key Constants with controller specific values
    def _INIT_EVENTKEY(self):
        # Defining Axis Event-Key Constants
        self.EVENTKEY.AXIS_EVENT = 'Absolute'   # Axis Event
        self.EVENTKEY.JOYL_X = 'ABS_X'          # Joystick Left - Axis X
        self.EVENTKEY.JOYL_Y = 'ABS_Y'          # Joystick Left - Axis Y
        self.EVENTKEY.JOYR_X = 'ABS_RX'         # Joystick Right - Axis X
        self.EVENTKEY.JOYR_Y = 'ABS_RY'         # Joystick Right - Axis Y
        self.EVENTKEY.TRIG_L = 'ABS_Z'          # Trigger Left - Axis
        self.EVENTKEY.TRIG_R = 'ABS_RZ'         # Trigger Right - Axis

        # Defining Button Event-Key Constants
        self.EVENTKEY.BTN_EVENT = 'Key'         # Button Event
        self.EVENTKEY.DPAD_X = 'ABS_HAT0X'      # D-Pad - Axis X
        self.EVENTKEY.DPAD_Y = 'ABS_HAT0Y'      # D-Pad - Axis Y
        self.EVENTKEY.DPAD_L = ''               # D-Pad - Left
        self.EVENTKEY.DPAD_R = ''               # D-Pad - Right
        self.EVENTKEY.DPAD_U = ''               # D-Pad - Up
        self.EVENTKEY.DPAD_D = ''               # D-Pad - Down
        self.EVENTKEY.BTN_A = 'BTN_SOUTH'       # Button - A
        self.EVENTKEY.BTN_B = 'BTN_EAST'        # Button - B
        self.EVENTKEY.BTN_X = 'BTN_WEST'        # Button - X
        self.EVENTKEY.BTN_Y = 'BTN_NORTH'       # Button - Y
        self.EVENTKEY.BTN_LB = 'BTN_TL'         # Button - Left-Back
        self.EVENTKEY.BTN_RB = 'BTN_TR'         # Button - Right-Back   
        self.EVENTKEY.BTN_LB2 = ' '             # Button - Left-Back Trigger
        self.EVENTKEY.BTN_RB2 = ' '             # Button - Right-Back Trigger
        self.EVENTKEY.BTN_PBL = 'BTN_THUMBL'    # Button - Joystick Left Push
        self.EVENTKEY.BTN_PBR = 'BTN_THUMBR'    # Button - Joystick Right Push
        self.EVENTKEY.BTN_START = 'BTN_START'   # Button - Start
        self.EVENTKEY.BTN_SELECT = 'BTN_SELECT' # Button - Select

    # Overwrite Joystick Scaling Constants with controller specific values
    def _INIT_JOYSCALE(self):
        # Defining Joystick Scaling Constants
        self.JOYSCALE.JOY_RAW_MIN = -32768  # Joystick Minimum Raw value
        self.JOYSCALE.JOY_RAW_MAX = 32767   # Joystick Maximum Raw value
        self.JOYSCALE.JOY_RAW_DB = 1000     # Joystick Deadband Raw value
        self.JOYSCALE.JOY_MIN = -100.0      # Joystick Minimum Scaling value
        self.JOYSCALE.JOY_MAX = 100.0       # Joystick Maximum Scaling value

    # Overwrite Trigger Scaling Constants with controller specific values
    def _INIT_TRIGSCALE(self):
        # Defining Trigger Scaling Constants
        self.TRIGSCALE.TRIG_RAW_MIN = 0     # Joystick Minimum Raw value
        self.TRIGSCALE.TRIG_RAW_MAX = 255   # Joystick Maximum Raw value
        self.TRIGSCALE.TRIG_RAW_DB = 0      # Joystick Deadband Raw value
        self.TRIGSCALE.TRIG_MIN = 0.0       # Joystick Minimum Scaling value
        self.TRIGSCALE.TRIG_MAX = 100.0     # Joystick Maximum Scaling value

# Dataclass - PS3 Controller
# ------------------------------
@dataclass
class PS3_CONST(_GAMEPAD_CONST):
    """
    PS3 - Controller Constants:
    Inherits and uses the default gamepad controller constant dataclass
    and overwrites certain constant values to match the related specific controller type
    """

    def __post_init__(self) -> None:
        # Initialize
        self._INIT_EVENTKEY()
        self._INIT_JOYSCALE()
        self._INIT_TRIGSCALE()
    
    # Overwrite Event-Key Constants with controller specific values
    def _INIT_EVENTKEY(self):
         # Defining Axis Event-Key Constants
        self.EVENTKEY.AXIS_EVENT = 'Absolute'   # Axis Event
        self.EVENTKEY.JOYL_X = 'ABS_X'          # Joystick Left - Axis X
        self.EVENTKEY.JOYL_Y = 'ABS_Y'          # Joystick Left - Axis Y
        self.EVENTKEY.JOYR_X = 'ABS_RX'         # Joystick Right - Axis X
        self.EVENTKEY.JOYR_Y = 'ABS_RY'         # Joystick Right - Axis Y
        self.EVENTKEY.TRIG_L = 'ABS_Z'          # Trigger Left - Axis
        self.EVENTKEY.TRIG_R = 'ABS_RZ'         # Trigger Right - Axis

        # Defining Button Event-Key Constants
        self.EVENTKEY.BTN_EVENT = 'Key'         # Button Event
        self.EVENTKEY.DPAD_X = ''               # D-Pad - Axis X
        self.EVENTKEY.DPAD_Y = ''               # D-Pad - Axis Y
        self.EVENTKEY.DPAD_L = 'BTN_DPAD_LEFT'  # D-Pad - Left
        self.EVENTKEY.DPAD_R = 'BTN_DPAD_RIGHT' # D-Pad - Right
        self.EVENTKEY.DPAD_U = 'BTN_DPAD_UP'    # D-Pad - Up
        self.EVENTKEY.DPAD_D = 'BTN_DPAD_DOWN'  # D-Pad - Down
        self.EVENTKEY.BTN_A = 'BTN_SOUTH'       # Button - A
        self.EVENTKEY.BTN_B = 'BTN_EAST'        # Button - B
        self.EVENTKEY.BTN_X = 'BTN_WEST'        # Button - X
        self.EVENTKEY.BTN_Y = 'BTN_NORTH'       # Button - Y
        self.EVENTKEY.BTN_LB = 'BTN_TL'         # Button - Left-Back
        self.EVENTKEY.BTN_RB = 'BTN_TR'         # Button - Right-Back   
        self.EVENTKEY.BTN_LB2 = 'BTN_TL2'       # Button - Left-Back Trigger
        self.EVENTKEY.BTN_RB2 = 'BTN_TR2'       # Button - Right-Back Trigger
        self.EVENTKEY.BTN_PBL = 'BTN_THUMBL'    # Button - Joystick Left Push
        self.EVENTKEY.BTN_PBR = 'BTN_THUMBR'    # Button - Joystick Right Push
        self.EVENTKEY.BTN_START = 'BTN_START'   # Button - Start
        self.EVENTKEY.BTN_SELECT = 'BTN_SELECT' # Button - Select

    # Overwrite Joystick Scaling Constants with controller specific values
    def _INIT_JOYSCALE(self):
        # Defining Joystick Scaling Constants
        self.JOYSCALE.JOY_RAW_MIN = -32768  # Joystick Minimum Raw value
        self.JOYSCALE.JOY_RAW_MAX = 32767   # Joystick Maximum Raw value
        self.JOYSCALE.JOY_RAW_DB = 1000     # Joystick Deadband Raw value
        self.JOYSCALE.JOY_MIN = -100.0      # Joystick Minimum Scaling value
        self.JOYSCALE.JOY_MAX = 100.0       # Joystick Maximum Scaling value

    # Overwrite Trigger Scaling Constants with controller specific values
    def _INIT_TRIGSCALE(self):
        # Defining Trigger Scaling Constants
        self.TRIGSCALE.TRIG_RAW_MIN = 0     # Joystick Minimum Raw value
        self.TRIGSCALE.TRIG_RAW_MAX = 255   # Joystick Maximum Raw value
        self.TRIGSCALE.TRIG_RAW_DB = 0      # Joystick Deadband Raw value
        self.TRIGSCALE.TRIG_MIN = 0.0       # Joystick Minimum Scaling value
        self.TRIGSCALE.TRIG_MAX = 100.0     # Joystick Maximum Scaling value

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

# XBOX Controller - Axis Event
# ------------------------------
def XBOX_AxisEvent(event : any, 
                   XBOXONE_CONST : XBOXONE_CONST, 
                   axisData : _AxisData):
    """
    XBOX Controller
    Get incomming Axis-Events from Controller-Input (integer values)
    :param event: Element of Events from Connected Gamepad object
    :param XBOXONE_CONST: XBOX Controller Constants (_XBOXONE_CONST)
    :return param Axis: Axis-Dataclass (_AXIS)
    """

    # Axis Event
    # Incomming Axis-Input from Controller (integer values)
    if event.ev_type == XBOXONE_CONST.EVENTKEY.AXIS_EVENT:
        
        # Joystick Left - Axis X
        if event.code == XBOXONE_CONST.EVENTKEY.JOYL_X:
            axisData.JoyL_X = event.state

        # Joystick Left - Axis Y
        elif event.code == XBOXONE_CONST.EVENTKEY.JOYL_Y:
            axisData.JoyL_Y = event.state

        # Joystick Right - Axis X
        elif event.code == XBOXONE_CONST.EVENTKEY.JOYR_X:
            axisData.JoyR_X = event.state

        # Joystick Right - Axis Y
        elif event.code == XBOXONE_CONST.EVENTKEY.JOYR_Y:
            axisData.JoyR_Y = event.state

        # Trigger Left - Axis
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_L:
            axisData.Trig_L = event.state

        # Trigger Right - Axis
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_R:
            axisData.Trig_R = event.state

    # Function return
    return axisData

# XBOX Controller - Button Event
# ------------------------------
def XBOX_ButtonEvent(event : any, 
                     XBOXONE_CONST : XBOXONE_CONST, 
                     buttonData : _ButtonData):
    """
    XBOX Controller
    Get incomming Button-Events from Controller-Input (bool values)
    :param event: Element of Events from Connected Gamepad object
    :param XBOXONE_CONST: XBOX Controller Constants (_XBOXONE_CONST)
    :return param Button: Button-Dataclass (_Button)
    """

    # Button Event
    # Incomming Button-Input from Controller (bool values)
    if event.ev_type == XBOXONE_CONST.EVENTKEY.BTN_EVENT:
        
        # Button - A
        if event.code == XBOXONE_CONST.EVENTKEY.BTN_A:
            buttonData.A = event.state

        # Button - B
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_B:
            buttonData.B = event.state

        # Button - X
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_X:
            buttonData.X = event.state

        # Button - Y
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_Y:
            buttonData.Y = event.state

        # Button - Left-Back
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_LB:
            buttonData.LB = event.state

        # Button - Right-Back
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_RB:
            buttonData.RB = event.state

        # Button - Joystick Left Push
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_PBL:
            buttonData.PB_L = event.state

        # Button - Joystick Right Push
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_PBR:
            buttonData.PB_R = event.state

        # Button - Start
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_START:
            buttonData.Start = event.state

        # Button - Select
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_SELECT:
            buttonData.Select = event.state

    # Axis Event
    # Special case for D-PAD and Trigger buttons
    if event.ev_type == XBOXONE_CONST.EVENTKEY.AXIS_EVENT:

        # D-PAD - Left / Right
        if event.code == XBOXONE_CONST.EVENTKEY.DPAD_X:
            
            # Determine Left/Right by sign of state-value
            if event.state < 0:
                buttonData.DPad_L = 1

            elif event.state > 0:
                buttonData.DPad_R = 1

            # Reset D-PAD - Left / Right values
            else:
                buttonData.DPad_L = 0
                buttonData.DPad_R = 0
            
        # D-PAD - Up / Down
        elif event.code == XBOXONE_CONST.EVENTKEY.DPAD_Y:

            # Determine Up/Down by sign of state-value
            if event.state < 0:
                buttonData.DPad_U = 1

            elif event.state > 0:
                buttonData.DPad_D = 1

            # Reset D-PAD - Up / Down values
            else:
                buttonData.DPad_U = 0
                buttonData.DPad_D = 0

        # Button - Left-Back Trigger
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_L:

            # Determine if active
            if event.state > 0:
                buttonData.LB2 = 1

            # Reset Left-Back Trigger
            else:
                buttonData.LB2 = 0

        # Button - Right-Back Trigger
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_R:

            # Determine if active
            if event.state > 0:
                buttonData.RB2 = 1

            # Reset Left-Back Trigger
            else:
                buttonData.RB2 = 0

    # Function return
    return buttonData

# PS3 Controller - Axis Event
# ------------------------------
def PS3_AxisEvent(event : any, 
                   PS3_CONST : PS3_CONST, 
                   axisData : _AxisData):
    """
    PS3 Controller
    Get incomming Axis-Events from Controller-Input (integer values)
    :param event: Element of Events from Connected Gamepad object
    :param PS3_CONST: PS3 Controller Constants (_PS3_CONST)
    :return param Axis: Axis-Dataclass (_AXIS)
    """

    # Axis Event
    # Incomming Axis-Input from Controller (integer values)
    if event.ev_type == PS3_CONST.EVENTKEY.AXIS_EVENT:
        
        # Joystick Left - Axis X
        if event.code == PS3_CONST.EVENTKEY.JOYL_X:
            axisData.JoyL_X = event.state

        # Joystick Left - Axis Y
        elif event.code == PS3_CONST.EVENTKEY.JOYL_Y:
            axisData.JoyL_Y = event.state

        # Joystick Right - Axis X
        elif event.code == PS3_CONST.EVENTKEY.JOYR_X:
            axisData.JoyR_X = event.state

        # Joystick Right - Axis Y
        elif event.code == PS3_CONST.EVENTKEY.JOYR_Y:
            axisData.JoyR_Y = event.state

        # Trigger Left - Axis
        elif event.code == PS3_CONST.EVENTKEY.TRIG_L:
            axisData.Trig_L = event.state

        # Trigger Right - Axis
        elif event.code == PS3_CONST.EVENTKEY.TRIG_R:
            axisData.Trig_R = event.state

    # Function return
    return axisData

# PS3 Controller - Button Event
# ------------------------------
def PS3_ButtonEvent(event : any, 
                     PS3_CONST : PS3_CONST, 
                     buttonData : _ButtonData):
    """
    PS3 Controller
    Get incomming Button-Events from Controller-Input (bool values)
    :param event: Element of Events from Connected Gamepad object
    :param PS3_CONST: PS3 Controller Constants (_PS3_CONST)
    :return param Button: Button-Dataclass (_Button)
    """

    # Button Event
    # Incomming Button-Input from Controller (bool values)
    if event.ev_type == PS3_CONST.EVENTKEY.BTN_EVENT:
        
        # Button - A
        if event.code == PS3_CONST.EVENTKEY.BTN_A:
            buttonData.A = event.state

        # Button - B
        elif event.code == PS3_CONST.EVENTKEY.BTN_B:
            buttonData.B = event.state

        # Button - X
        elif event.code == PS3_CONST.EVENTKEY.BTN_X:
            buttonData.X = event.state

        # Button - Y
        elif event.code == PS3_CONST.EVENTKEY.BTN_Y:
            buttonData.Y = event.state

        # Button - Left-Back
        elif event.code == PS3_CONST.EVENTKEY.BTN_LB:
            buttonData.LB = event.state

        # Button - Right-Back
        elif event.code == PS3_CONST.EVENTKEY.BTN_RB:
            buttonData.RB = event.state

        # Button - Joystick Left Push
        elif event.code == PS3_CONST.EVENTKEY.BTN_PBL:
            buttonData.PB_L = event.state

        # Button - Joystick Right Push
        elif event.code == PS3_CONST.EVENTKEY.BTN_PBR:
            buttonData.PB_R = event.state

        # Button - Start
        elif event.code == PS3_CONST.EVENTKEY.BTN_START:
            buttonData.Start = event.state

        # Button - Select
        elif event.code == PS3_CONST.EVENTKEY.BTN_SELECT:
            buttonData.Select = event.state

        # D-PAD - Left
        if event.code == PS3_CONST.EVENTKEY.DPAD_L:
            buttonData.DPad_L = event.state

        # D-PAD - Right
        elif event.code == PS3_CONST.EVENTKEY.DPAD_R:
            buttonData.DPad_R = event.state

        # D-PAD - Up
        elif event.code == PS3_CONST.EVENTKEY.DPAD_U:
            buttonData.DPad_U = event.state

        # D-PAD - Down
        elif event.code == PS3_CONST.EVENTKEY.DPAD_D:
            buttonData.DPad_D = event.state

        # Button - Left-Back Trigger
        elif event.code == PS3_CONST.EVENTKEY.BTN_LB2:
            buttonData.LB2 = event.state

        # Button - Right-Back Trigger
        elif event.code == PS3_CONST.EVENTKEY.BTN_RB2:
            buttonData.RB2 = event.state

    # Function return
    return buttonData

# Scale Input Value
# -----------------------------
def calcMinMaxScaling(raw_value : int,
                        raw_min : int,
                        raw_max : int,
                        min : float,
                        max : float):
    """
    Rescale the raw input value from range [raw_min, raw_max] to a desired range [min, max]
    :param raw_value: Raw Input Value
    :param raw_min: Raw Minimum Value
    :param raw_max: Raw Maximum Value
    :param min: Scaled Minimum value
    :param max: Scaled Maximum value
    :return value: Scaled Value
    """

    # Scaling input-value to range: [0 , 1]
    tmp_value = (raw_value - raw_min) / (raw_max - raw_min)

    # Scaling input-value to range: [min , max]
    value = tmp_value * (max - min) + min

    return value

# Scale Input Value with Deadband
# -----------------------------
def calcMinMaxScaling_DB(raw_value : int,
                            raw_min : int,
                            raw_max : int,
                            raw_db : int,
                            min : float,
                            max : float):
    """
    Rescale the raw input value from range [raw_min, raw_max] to a desired range [min, max]
    with neglecting Deadband value on the raw input value 
    :param raw_value: Raw Input Value
    :param raw_min: Raw Minimum Value
    :param raw_max: Raw Maximum Value
    :param raw_db:  Raw Deadband Value
    :param min: Scaled Minimum value
    :param max: Scaled Maximum value
    :return value: Scaled Value
    """

    # Use local variable
    tmp_raw_value = 0
    tmp_raw_min = raw_min + raw_db
    tmp_raw_max = raw_max - raw_db
    tmp_raw_db_neg = (-1) * raw_db 
    tmp_raw_db_pos = raw_db

    # Deadband Calculation
    # -----------------------------
    # Raw value is whithin deadband range
    if (abs(raw_value) < abs(raw_db)):
        tmp_raw_value = 0

    # Raw value is below deadband range
    elif (raw_value < tmp_raw_db_neg):
        tmp_raw_value = raw_value + raw_db

    # Raw value is above deadband range
    elif (raw_value > tmp_raw_db_pos):
        tmp_raw_value = raw_value - raw_db

    # Rescaling
    # -----------------------------
    # Scaling input-value to range: [0 , 1]
    tmp_value = (tmp_raw_value - tmp_raw_min) / (tmp_raw_max - tmp_raw_min)

    # Scaling input-value to range: [min , max]
    value = tmp_value * (max - min) + min

    return value

# Scale Joystick Input Value with Deadband
# -----------------------------
def scaleJoystickInput(raw_value : int,
                        JOY_SCALE : _JOYSCALE):
    """
    Rescale the raw Joystick input value from range [raw_min, raw_max] to a desired range [min, max]
    with neglecting Joystick Deadband 
    :param raw_value: Raw Input Value
    :param JOY_SCALE: Joystick Scaling Constans Dataclass 
    :return value: Scaled Value
    """
    
    joy_value = calcMinMaxScaling_DB(raw_value, 
                                    JOY_SCALE.JOY_RAW_MIN,
                                    JOY_SCALE.JOY_RAW_MAX,
                                    JOY_SCALE.JOY_RAW_DB,
                                    JOY_SCALE.JOY_MIN,
                                    JOY_SCALE.JOY_MAX)
    
    return joy_value

# Scale Trigger Input Value with Deadband
# -----------------------------
def scaleTriggerInput(raw_value : int,
                    TRIG_SCALE : _TRIGSCALE):
    """
    Rescale the raw Trigger input value from range [raw_min, raw_max] to a desired range [min, max]
    with neglecting Trigger Deadband 
    :param raw_value: Raw Input Value
    :param TRIG_SCALE: Trigger Scaling Constans Dataclass 
    :return value: Scaled Value
    """
    
    trigger_value = calcMinMaxScaling_DB(raw_value, 
                                        TRIG_SCALE.TRIG_RAW_MIN,
                                        TRIG_SCALE.TRIG_RAW_MAX,
                                        TRIG_SCALE.TRIG_RAW_DB,
                                        TRIG_SCALE.TRIG_MIN,
                                        TRIG_SCALE.TRIG_MAX)
    
    return trigger_value