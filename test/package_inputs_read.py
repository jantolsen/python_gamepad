from inputs import get_gamepad
from inputs import devices

def main():

    # Get devices
    all_gamepads = devices.gamepads
    print(len(all_gamepads)) # Print number of gamepads

    # Get first device
    gamepad_no1 = devices.gamepads[0]
    print(gamepad_no1)
    print(type(gamepad_no1))

    # FIND TYPE
    xbox_type = 'Microsoft'
    ps3_type = 'PLAYSTATION'
    gamepad_type = format(gamepad_no1)
    # Check type
    if xbox_type in gamepad_type:
        print('XBOX')
    elif ps3_type in gamepad_type:
        print('PS3')
    else:
        print('unknown')

    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:

            if event.ev_type == 'Absolute':
            # if event.ev_type == 'Key':

                print(event.ev_type, event.code, event.state)


if __name__ == "__main__":
    main()