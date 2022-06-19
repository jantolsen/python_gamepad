from inputs import get_gamepad


def main():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
            # if event.ev_type == 'Key':
                print(event.ev_type, event.code, event.state)


if __name__ == "__main__":
    main()