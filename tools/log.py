from pythonConsoleConfigs.Font import Style


def cPrint(msg, color, reset=True):
    if reset:
        print(msg[0] + color + msg[1])
        Style().reset()
    else:
        print(msg[0] + color + msg[1])
