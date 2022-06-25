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
import controller_toolbox as ControllerToolbox

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
    Trig_L : float = 0.0    # Trigger Left - Axis
    Trig_R : float = 0.0    # Trigger Left - Axis

# Dataclass - Buttons 
# ------------------------------
# Members related to Controller Buttons
@dataclass
class _ButtonData:
    
    # Declare Button members
    S : bool = 0        # Button - South
    E : bool = 0        # Button - East
    W : bool = 0        # Button - West
    N : bool = 0        # Button - North
    
    Start : bool = 0    # Button - Start
    Select : bool = 0   # Button - Select

    PB_L : bool = 0     # Joystick Left - Pushbutton
    PB_R : bool = 0     # Joystick Right - Pushbutton

    DPad_L : bool = 0   # D-Pad - Left
    DPad_R : bool = 0   # D-Pad - Right
    DPad_U : bool = 0   # D-Pad - Up
    DPad_D : bool = 0   # D-Pad - Down

    LB1: bool = 0       # Button - Left-Back Bumper No. 1
    RB1: bool = 0       # Button - Right-Back Bumper No. 1
    LB2: bool = 0       # Button - Left-Back Bumper No. 2
    RB2: bool = 0       # Button - Right-Back Bumper No. 2

# Dataclass - Joystick Data
# ------------------------------
# Member to hold Controller Input
@dataclass
class _JoyData:
    # Define Joystick Data members
    X   : int = 0   # Joystick - X-Axis
    Y   : int = 0   # Joystick - Y-Axis
    PB  : bool = 0  # Joystick - Pushbutton

# Dataclass - Directional-Pad Data
# ------------------------------
# Member to hold Controller Input
@dataclass
class _DPadData:
    # Define Joystick Data members
    L  : bool = 0   # D-Pad - Left
    R  : bool = 0   # D-Pad - Right
    U  : bool = 0   # D-Pad - Up
    D  : bool = 0   # D-Pad - Down

# Dataclass - Trigger Data
# ------------------------------
# Member to hold Controller Input
@dataclass
class _TrigData:
    # Define Trigger Data members
    VAL : int = 0   # Trigger - Value
    B1  : bool = 0  # Back Bumper No. 1
    B2  : bool = 0  # Back Bumper No. 2

# Dataclass - Button Data (XBOX)
# ------------------------------
# Member to hold Controller Input
@dataclass
class _XBOX_ButtonData:
    # Define Button Data members
    A : bool = 0        # Button - A
    B : bool = 0        # Button - B
    X : bool = 0        # Button - X
    Y : bool = 0        # Button - Y
    Start : bool = 0    # Button - Start
    Select : bool = 0   # Button - Select

# Dataclass - Button Data (PS)
# ------------------------------
# Member to hold Controller Input
@dataclass
class _PS_ButtonData:
    # Define Button Data members
    Cross       : bool = 0  # Button - Cross
    Circle      : bool = 0  # Button - Circle
    Triangle    : bool = 0  # Button - Triangle
    Square      : bool = 0  # Button - Square
    Start       : bool = 0  # Button - Start
    Select      : bool = 0  # Button - Select

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
    BTN_S       : str = field(init=False)   # Button - South
    BTN_E       : str = field(init=False)   # Button - East
    BTN_W       : str = field(init=False)   # Button - West
    BTN_N       : str = field(init=False)   # Button - North
    BTN_LB1     : str = field(init=False)   # Button - Left-Back Bumper No. 1
    BTN_RB1     : str = field(init=False)   # Button - Right-Back Bumper No. 1   
    BTN_LB2     : str = field(init=False)   # Button - Left-Back Bumper No. 2
    BTN_RB2     : str = field(init=False)   # Button - Right-Back Bumper No. 2  
    BTN_PBL     : str = field(init=False)   # Button - Joystick Left Push
    BTN_PBR     : str = field(init=False)   # Button - Joystick Right Push
    BTN_START   : str = field(init=False)   # Button - Start
    BTN_SELECT  : str = field(init=False)   # Button - Select

# Dataclass - Controller Joystick Scaling Constans
# ------------------------------
@dataclass
class _JOY_SCALING():
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
class _TRIG_SCALING():
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
    :param (optional) _JOY_SCALING:   Joystick Scaling Constants
    :param (optional) _TRIG_SCALING:  Trigger Scaling Constants
    """
    # XBOX-One Constants
    EVENTKEY        : _EVENTKEY = field(init=False, default_factory = _EVENTKEY)         
    JOY_SCALING     : _JOY_SCALING = field(init=False, default_factory = _JOY_SCALING)
    TRIG_SCALING    : _TRIG_SCALING = field(init=False, default_factory = _TRIG_SCALING)

    def __post_init__(self) -> None:
        # Initialize
        self._INIT_EVENTKEY()
        self._INIT_JOY_SCALING()
        self._INIT_TRIG_SCALING()
    
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
        self.EVENTKEY.BTN_S = 'BTN_SOUTH'       # Button - A
        self.EVENTKEY.BTN_E = 'BTN_EAST'        # Button - B
        self.EVENTKEY.BTN_W = 'BTN_WEST'        # Button - X
        self.EVENTKEY.BTN_N = 'BTN_NORTH'       # Button - Y
        self.EVENTKEY.BTN_LB1 = 'BTN_TL'        # Button - Left-Back Bumper No. 1
        self.EVENTKEY.BTN_RB1 = 'BTN_TR'        # Button - Right-Back Bumper No. 1   
        self.EVENTKEY.BTN_LB2 = 'BTN_TL2'       # Button - Left-Back Bumper No. 2
        self.EVENTKEY.BTN_RB2 = 'BTN_TR2'       # Button - Right-Back Bumper No. 2

    def _INIT_JOY_SCALING(self):
        # Defining Joystick Scaling Constants
        self.JOY_SCALING.JOY_RAW_MIN = -32768  # Joystick Minimum Raw value
        self.JOY_SCALING.JOY_RAW_MAX = 32767   # Joystick Maximum Raw value
        self.JOY_SCALING.JOY_RAW_DB = 1000     # Joystick Deadband Raw value
        self.JOY_SCALING.JOY_MIN = -100.0      # Joystick Minimum Scaling value
        self.JOY_SCALING.JOY_MAX = 100.0       # Joystick Maximum Scaling value

    def _INIT_TRIG_SCALING(self):
        # Defining Trigger Scaling Constants
        self.TRIG_SCALING.TRIG_RAW_MIN = 0     # Joystick Minimum Raw value
        self.TRIG_SCALING.TRIG_RAW_MAX = 255   # Joystick Maximum Raw value
        self.TRIG_SCALING.TRIG_RAW_DB = 0      # Joystick Deadband Raw value
        self.TRIG_SCALING.TRIG_MIN = 0.0       # Joystick Minimum Scaling value
        self.TRIG_SCALING.TRIG_MAX = 100.0     # Joystick Maximum Scaling value

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
        self._INIT_JOY_SCALING()
        self._INIT_TRIG_SCALING()
    
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
        self.EVENTKEY.BTN_S = 'BTN_SOUTH'       # Button - South
        self.EVENTKEY.BTN_E = 'BTN_EAST'        # Button - East
        self.EVENTKEY.BTN_W = 'BTN_WEST'        # Button - West
        self.EVENTKEY.BTN_N = 'BTN_NORTH'       # Button - North
        self.EVENTKEY.BTN_LB1 = 'BTN_TL'        # Button - Left-Back Bumper No. 1
        self.EVENTKEY.BTN_RB1 = 'BTN_TR'        # Button - Right-Back Bumper No. 1  
        self.EVENTKEY.BTN_LB2 = ' '             # Button - Left-Back Bumper No. 2
        self.EVENTKEY.BTN_RB2 = ' '             # Button - Right-Back Bumper No. 2
        self.EVENTKEY.BTN_PBL = 'BTN_THUMBL'    # Button - Joystick Left Push
        self.EVENTKEY.BTN_PBR = 'BTN_THUMBR'    # Button - Joystick Right Push
        self.EVENTKEY.BTN_START = 'BTN_START'   # Button - Start
        self.EVENTKEY.BTN_SELECT = 'BTN_SELECT' # Button - Select

    # Overwrite Joystick Scaling Constants with controller specific values
    def _INIT_JOY_SCALING(self):
        # Defining Joystick Scaling Constants
        self.JOY_SCALING.JOY_RAW_MIN = -32768  # Joystick Minimum Raw value
        self.JOY_SCALING.JOY_RAW_MAX = 32767   # Joystick Maximum Raw value
        self.JOY_SCALING.JOY_RAW_DB = 1000     # Joystick Deadband Raw value
        self.JOY_SCALING.JOY_MIN = -100.0      # Joystick Minimum Scaling value
        self.JOY_SCALING.JOY_MAX = 100.0       # Joystick Maximum Scaling value

    # Overwrite Trigger Scaling Constants with controller specific values
    def _INIT_TRIG_SCALING(self):
        # Defining Trigger Scaling Constants
        self.TRIG_SCALING.TRIG_RAW_MIN = 0     # Joystick Minimum Raw value
        self.TRIG_SCALING.TRIG_RAW_MAX = 255   # Joystick Maximum Raw value
        self.TRIG_SCALING.TRIG_RAW_DB = 0      # Joystick Deadband Raw value
        self.TRIG_SCALING.TRIG_MIN = 0.0       # Joystick Minimum Scaling value
        self.TRIG_SCALING.TRIG_MAX = 100.0     # Joystick Maximum Scaling value

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
        self._INIT_JOY_SCALING()
        self._INIT_TRIG_SCALING()
    
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
        self.EVENTKEY.BTN_S = 'BTN_SOUTH'       # Button - South
        self.EVENTKEY.BTN_E = 'BTN_EAST'        # Button - East
        self.EVENTKEY.BTN_W = 'BTN_WEST'        # Button - West
        self.EVENTKEY.BTN_N = 'BTN_NORTH'       # Button - North
        self.EVENTKEY.BTN_LB1 = 'BTN_TL'        # Button - Left-Back Bumper No. 1
        self.EVENTKEY.BTN_RB1 = 'BTN_TR'        # Button - Right-Back Bumper No. 1   
        self.EVENTKEY.BTN_LB2 = 'BTN_TL2'       # Button - Left-Back Bumper No. 2   
        self.EVENTKEY.BTN_RB2 = 'BTN_TR2'       # Button - Right-Back Bumper No. 2 
        self.EVENTKEY.BTN_PBL = 'BTN_THUMBL'    # Button - Joystick Left Push
        self.EVENTKEY.BTN_PBR = 'BTN_THUMBR'    # Button - Joystick Right Push
        self.EVENTKEY.BTN_START = 'BTN_START'   # Button - Start
        self.EVENTKEY.BTN_SELECT = 'BTN_SELECT' # Button - Select

    # Overwrite Joystick Scaling Constants with controller specific values
    def _INIT_JOY_SCALING(self):
        # Defining Joystick Scaling Constants
        self.JOY_SCALING.JOY_RAW_MIN = -32768  # Joystick Minimum Raw value
        self.JOY_SCALING.JOY_RAW_MAX = 32767   # Joystick Maximum Raw value
        self.JOY_SCALING.JOY_RAW_DB = 1000     # Joystick Deadband Raw value
        self.JOY_SCALING.JOY_MIN = -100.0      # Joystick Minimum Scaling value
        self.JOY_SCALING.JOY_MAX = 100.0       # Joystick Maximum Scaling value

    # Overwrite Trigger Scaling Constants with controller specific values
    def _INIT_TRIG_SCALING(self):
        # Defining Trigger Scaling Constants
        self.TRIG_SCALING.TRIG_RAW_MIN = 0     # Joystick Minimum Raw value
        self.TRIG_SCALING.TRIG_RAW_MAX = 255   # Joystick Maximum Raw value
        self.TRIG_SCALING.TRIG_RAW_DB = 0      # Joystick Deadband Raw value
        self.TRIG_SCALING.TRIG_MIN = 0.0       # Joystick Minimum Scaling value
        self.TRIG_SCALING.TRIG_MAX = 100.0     # Joystick Maximum Scaling value

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
                   JoyL : _JoyData,
                   JoyR : _JoyData,
                   TrigL : _TrigData,
                   TrigR : _TrigData,
                   AxisData : _AxisData):
    """
    XBOX Controller
    Get incomming Axis-Events from Controller-Input (integer values)
    :param event: Element of Events from Connected Gamepad object
    :param XBOXONE_CONST: XBOX Controller Constants (_XBOXONE_CONST)
    :return param JoyL: Joystick-Left-Data Dataclass (_Joy_Data)
    :return param JoyR: Joystick-Rigth-Data Dataclass (_Joy_Data)
    :return param JoyL: Trigger-Left-Data Dataclass (_Trig_Data)
    :return param JoyL: Trigger-Right-Data Dataclass (_Trig_Data)
    """

    # Axis Event
    # Incomming Axis-Input from Controller (integer values)
    if event.ev_type == XBOXONE_CONST.EVENTKEY.AXIS_EVENT:
        
        # Joystick Left - Axis X
        if event.code == XBOXONE_CONST.EVENTKEY.JOYL_X:
            JoyL.X = event.state
            AxisData.JoyL_X = event.state

        # Joystick Left - Axis Y
        elif event.code == XBOXONE_CONST.EVENTKEY.JOYL_Y:
            JoyL.Y = event.state
            AxisData.JoyL_Y = event.state

        # Joystick Right - Axis X
        elif event.code == XBOXONE_CONST.EVENTKEY.JOYR_X:
            JoyR.X = event.state
            AxisData.JoyR_X = event.state

        # Joystick Right - Axis Y
        elif event.code == XBOXONE_CONST.EVENTKEY.JOYR_Y:
            JoyR.Y = event.state
            AxisData.JoyR_Y = event.state

        # Trigger Left - Axis
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_L:
            TrigL.VAL = event.state
            AxisData.Trig_L = event.state

        # Trigger Right - Axis
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_R:
            TrigL.VAL = event.state
            AxisData.Trig_R = event.state

# XBOX Controller - Button Event
# ------------------------------
def XBOX_ButtonEvent(event : any, 
                    XBOXONE_CONST : XBOXONE_CONST, 
                    JoyL : _JoyData,
                    JoyR : _JoyData,
                    TrigL : _TrigData,
                    TrigR : _TrigData,
                    DPad : _DPadData,
                    Button : _XBOX_ButtonData,
                    ButtonData : _ButtonData):
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
        if event.code == XBOXONE_CONST.EVENTKEY.BTN_S:
            Button.A = event.state
            ButtonData.S = event.state

        # Button - B
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_E:
            Button.B = event.state
            ButtonData.E = event.state

        # Button - X
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_W:
            Button.X = event.state
            ButtonData.W = event.state

        # Button - Y
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_N:
            Button.Y = event.state
            ButtonData.N = event.state

        # Button - Left-Back Bumper No. 1
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_LB1:
            TrigL.B1 = event.state
            ButtonData.LB1 = event.state

        # Button - Right-Back Bumper No. 1
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_RB1:
            TrigR.B1 = event.state
            ButtonData.RB1 = event.state

        # Button - Joystick Left Push
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_PBL:
            JoyL.PB = event.state
            ButtonData.PB_L = event.state

        # Button - Joystick Right Push
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_PBR:
            JoyR.PB = event.state
            ButtonData.PB_R = event.state

        # Button - Start
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_START:
            Button.Start = event.state
            ButtonData.Start = event.state

        # Button - Select
        elif event.code == XBOXONE_CONST.EVENTKEY.BTN_SELECT:
            Button.Select = event.state
            ButtonData.Select = event.state

    # Axis Event
    # Special case for D-PAD and Trigger buttons
    if event.ev_type == XBOXONE_CONST.EVENTKEY.AXIS_EVENT:

        # D-PAD - Left / Right
        if event.code == XBOXONE_CONST.EVENTKEY.DPAD_X:
            
            # Determine Left/Right by sign of state-value
            if event.state < 0:
                DPad.L = 1
                ButtonData.DPad_L = event.state

            elif event.state > 0:
                DPad.R = 1
                ButtonData.DPad_R = event.state

            # Reset D-PAD - Left / Right values
            else:
                DPad.L = 0
                DPad.R = 0
                ButtonData.DPad_L = event.state
                ButtonData.DPad_R = event.state
            
        # D-PAD - Up / Down
        elif event.code == XBOXONE_CONST.EVENTKEY.DPAD_Y:

            # Determine Up/Down by sign of state-value
            if event.state < 0:
                DPad.U = 1
                ButtonData.DPad_U = event.state

            elif event.state > 0:
                DPad.D = 1
                ButtonData.DPad_D = event.state

            # Reset D-PAD - Up / Down values
            else:
                DPad.U = 0
                DPad.D = 0
                ButtonData.DPad_U = event.state
                ButtonData.DPad_D = event.state

        # Button - Left-Back Bumper No. 2  
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_L:

            # Determine if active
            if event.state > 0:
                TrigL.B2 = 1
                ButtonData.LB2 = event.state

            # Reset Left-Back Bumper No. 2  
            else:
                TrigL.B2 = 0
                ButtonData.LB2 = event.state

        # Button - Right-Back Bumper No. 2
        elif event.code == XBOXONE_CONST.EVENTKEY.TRIG_R:

            # Determine if active
            if event.state > 0:
                TrigR.B2 = 1
                ButtonData.RB2 = event.state

            # Reset Right-Back Bumper No. 2
            else:
                TrigR.B2 = 0
                ButtonData.RB2 = event.state

# PS3 Controller - Axis Event
# ------------------------------
def PS3_AxisEvent(event : any, 
                   PS3_CONST : PS3_CONST, 
                   JoyL : _JoyData,
                   JoyR : _JoyData,
                   TrigL : _TrigData,
                   TrigR : _TrigData,
                   AxisData : _AxisData):
    """
    PS3 Controller
    Get incomming Axis-Events from Controller-Input (integer values)
    :param event: Element of Events from Connected Gamepad object
    :param XBOXONE_CONST: XBOX Controller Constants (_XBOXONE_CONST)
    :return param JoyL: Joystick-Left-Data Dataclass (_Joy_Data)
    :return param JoyR: Joystick-Rigth-Data Dataclass (_Joy_Data)
    :return param JoyL: Trigger-Left-Data Dataclass (_Trig_Data)
    :return param JoyL: Trigger-Right-Data Dataclass (_Trig_Data)
    """

    # Axis Event
    # Incomming Axis-Input from Controller (integer values)
    if event.ev_type == PS3_CONST.EVENTKEY.AXIS_EVENT:
        
        # Joystick Left - Axis X
        if event.code == PS3_CONST.EVENTKEY.JOYL_X:
            JoyL.X = event.state
            AxisData.JoyL_X = event.state

        # Joystick Left - Axis Y
        elif event.code == PS3_CONST.EVENTKEY.JOYL_Y:
            JoyL.Y = event.state
            AxisData.JoyL_Y = event.state

        # Joystick Right - Axis X
        elif event.code == PS3_CONST.EVENTKEY.JOYR_X:
            JoyR.X = event.state
            AxisData.JoyR_X = event.state

        # Joystick Right - Axis Y
        elif event.code == PS3_CONST.EVENTKEY.JOYR_Y:
            JoyR.Y = event.state
            AxisData.JoyR_Y = event.state

        # Trigger Left - Axis
        elif event.code == PS3_CONST.EVENTKEY.TRIG_L:
            TrigL.VAL = event.state
            AxisData.Trig_L = event.state

        # Trigger Right - Axis
        elif event.code == PS3_CONST.EVENTKEY.TRIG_R:
            TrigR.VAL = event.state
            AxisData.Trig_R = event.state

# PS3 Controller - Button Event
# ------------------------------
def PS3_ButtonEvent(event : any, 
                    PS3_CONST : PS3_CONST, 
                    JoyL : _JoyData,
                    JoyR : _JoyData,
                    TrigL : _TrigData,
                    TrigR : _TrigData,
                    DPad : _DPadData,
                    Button : _PS_ButtonData,
                    ButtonData : _ButtonData):
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
        
        # Button - Cross
        if event.code == PS3_CONST.EVENTKEY.BTN_S:
            Button.Cross = event.state
            ButtonData.S = event.state

        # Button - Circle
        elif event.code == PS3_CONST.EVENTKEY.BTN_E:
            Button.Circle = event.state
            ButtonData.E = event.state

        # Button - Square
        elif event.code == PS3_CONST.EVENTKEY.BTN_W:
            Button.Square = event.state
            ButtonData.W = event.state

        # Button - Triangle
        elif event.code == PS3_CONST.EVENTKEY.BTN_N:
            Button.Triangle = event.state
            ButtonData.N = event.state

        # Button - Left-Back Bumper No. 1
        elif event.code == PS3_CONST.EVENTKEY.BTN_LB1:
            TrigL.B1 = event.state
            ButtonData.LB1 = event.state

        # Button - Right-Back Bumper No. 1 
        elif event.code == PS3_CONST.EVENTKEY.BTN_RB1:
            TrigR.B1 = event.state
            ButtonData.RB1 = event.state

        # Button - Joystick Left Push
        elif event.code == PS3_CONST.EVENTKEY.BTN_PBL:
            JoyL.PB = event.state
            ButtonData.PB_L = event.state

        # Button - Joystick Right Push
        elif event.code == PS3_CONST.EVENTKEY.BTN_PBR:
            JoyR.PB = event.state
            ButtonData.PB_R = event.state

        # Button - Start
        elif event.code == PS3_CONST.EVENTKEY.BTN_START:
            Button.Start = event.state
            ButtonData.Start = event.state

        # Button - Select
        elif event.code == PS3_CONST.EVENTKEY.BTN_SELECT:
            Button.Select = event.state
            ButtonData.Select = event.state

        # D-PAD - Left
        if event.code == PS3_CONST.EVENTKEY.DPAD_L:
            DPad.L = event.state
            ButtonData.DPad_L = event.state

        # D-PAD - Right
        elif event.code == PS3_CONST.EVENTKEY.DPAD_R:
            DPad.R = event.state
            ButtonData.DPad_R = event.state

        # D-PAD - Up
        elif event.code == PS3_CONST.EVENTKEY.DPAD_U:
            DPad.U = event.state
            ButtonData.DPad_U = event.state

        # D-PAD - Down
        elif event.code == PS3_CONST.EVENTKEY.DPAD_D:
            DPad.D= event.state
            ButtonData.DPad_D = event.state

        # Button - Left-Back Bumper No. 2 
        elif event.code == PS3_CONST.EVENTKEY.BTN_LB2:
            TrigL.B2 = event.state
            ButtonData.LB2 = event.state

        # Button - Right-Back Bumper No. 2 
        elif event.code == PS3_CONST.EVENTKEY.BTN_RB2:
            TrigR.B2 = event.state
            ButtonData.RB2 = event.state

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
                        JOY_SCALE : _JOY_SCALING):
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
                        TRIG_SCALE : _TRIG_SCALING):
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

# Joystick Class
# -----------------------------
# Based on Joystick-Data, assign values to members of Joystick Class
# with correct scaling obtained from Gamepad-Constant
class Joystick():
    """
    Jostick Class:
    Assign values to Joystick members based on incomming Joystick-Data
    Joystick values are calculated with correct scaling with data from Gamepad-Constants
    :param GAMEPAD_CONST: Controller Constants (_GAMEPAD_CONST)
    :param JoyData: Joystick Data (_Joy_Data)
    """
    # Class Constructor
    def __init__(self, GAMEPAD_CONST : _GAMEPAD_CONST, JoyData : _JoyData):

        # Class Input(s):
        self.X_raw = JoyData.X
        self.Y_raw = JoyData.Y
        self.PB = JoyData.PB
        self.JOY_SCALING = GAMEPAD_CONST.JOY_SCALING

        # Class Variables
        self.X = 0.0
        self.Y = 0.0
        self.PB = 0

        # Update Joystick Values
        self.updateValues(JoyData)

    # Update Joystick Values based on new Input data
    def updateValues(self, JoyData : _JoyData):
        # Update Class Inputs
        self.X_raw = JoyData.X
        self.Y_raw = JoyData.Y
        self.PB = JoyData.PB

        # Get Joystick Values
        self.getPushbuttonValue()
        self.getAxisValues()

    # Get Joystick Pushbutton Value
    def getPushbuttonValue(self):
        
        # Function Return
        return self.PB

    # Get Joystick Axis-X Value
    def getAxisXValue(self):
        # Scale Axis Value
        self.X = scaleJoystickInput(self.X_raw, self.JOY_SCALING)

        # Function Return
        return self.X    

    # Get Joystick Axis-Y Value
    def getAxisYValue(self):
        # Scale Axis Value
        self.Y = scaleJoystickInput(self.Y_raw, self.JOY_SCALING)

        # Function Return
        return self.Y   
    
    # Get Joystick Axis Values
    def getAxisValues(self):
        # Call internal get axis value
        self.X = self.getAxisXValue()
        self.Y = self.getAxisYValue()

        # Function Return
        return [self.X, self.Y]

# Main Function
# ------------------------------   
if __name__ == '__main__':
    # xbox_constants = _XBOXONE_CONST(_EVENTKEY, _JOYSCALE, _TRIG_SCALING)
    # xbox_constants = _XBOXONE_CONST()
    
    # xbox_constants.JOYSCALE.JOY_RAW_DB = 3000
    # # print(xboxOneConstants)
    # print(xbox_constants)
    # print(xbox_constants.JOYSCALE.JOY_RAW_MAX)
    # print(xbox_constants.JOYSCALE.JOY_RAW_DB)
    # print('\n')

    xboxConst = XBOXONE_CONST()
    joyL_data = _JoyData()



    print(xboxConst)
    print(xboxConst.JOY_SCALING.JOY_RAW_DB)
    print('\n')

    xboxConst.JOY_SCALING.JOY_RAW_DB = 5000
    joyL_data.X = 23185

    JoyL = Joystick(xboxConst, joyL_data)
    # JoyL.updateValues(joyL_data)

    print('Joystick:')
    print(JoyL)
    print("X-Axis: ", JoyL.X, " Raw Value: ", JoyL.X_raw)
    print("Y-Axis: ", JoyL.Y, " Raw Value: ", JoyL.Y_raw)
    print('\n')

    joyL_data.X = -23185
    JoyL.updateValues(joyL_data)

    print("X-Axis: ", JoyL.X, " Raw Value: ", JoyL.X_raw)
    print("Y-Axis: ", JoyL.Y, " Raw Value: ", JoyL.Y_raw)
    print('\n')

