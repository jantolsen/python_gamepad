from inputs import get_gamepad
from inputs import devices

def main():

    ctrls = devices.gamepads
    x = devices.gamepads[0]
    
    print(devices.gamepads[0])
    print(len(ctrls))
    print(type(x))

    print(x.name)
    strA = 'Microsoft'
    strB = format(x)
    if strA in strB:
        print('yes')
    else:
        print('no')

    events = get_gamepad()
    print(events)
    """Just print out some event infomation when the gamepad is used."""
    # while 1:
    #     events = get_gamepad()
    #     for event in events:
    #         if event.ev_type == 'Key':
    #             print(event.ev_type, event.code, event.state)


if __name__ == "__main__":
    main()