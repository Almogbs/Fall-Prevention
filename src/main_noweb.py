from fall_prevention_server import Server
from fall_prevention_modes import CollectMode, Position


NUM_CLIENTS = 1
PORT = 13380
IP = "192.168.6.232"
ADDR = (IP, PORT)

HEIGHT_MIN = 120
HEIGHT_MAX = 220
WEIGHT_MIN = 40
WEIGHT_MAX = 150


def getLabel() -> int:
    while(True):
        print("Choose Label (by the index):\n")
        print("0. Laying Center")
        print("1. Laying Left")
        print("2. Laying Right")
        print("3. Alarm Left")
        print("4. Alarm Right")
        label = input("Label -> ")
        try:
            label = int(label)
            if label in [p.value for p in Position]:
                return label
        except (TypeError, ValueError):
            print("ERROR: Invalid Lable. Please try again.")


def getHeight() -> int:
    while(1):
        height = input("Height -> ")
        try:
            height = int(height)
            if HEIGHT_MIN <= height <= HEIGHT_MAX:
                return height
        except (TypeError, ValueError):
            pass
        print("ERROR: Invalid Height. Please try again.")


def getWeight() -> int:
    while(1):
        weight = input("Weight -> ")
        try:
            weight = int(weight)
            if WEIGHT_MIN <= weight <= WEIGHT_MAX:
                return weight
        except (TypeError, ValueError):
            pass
        print("ERROR: Invalid Weight. Please try again.")


def getMode() -> CollectMode:
    return CollectMode(verbose=True, label=getLabel(), height=getHeight(), weight=getWeight())


def updateMode(server: Server) -> None:
    print("Done session for that label.")
    print("Kepp smapling with the same patient?\t Y/n")
    while(1):
        try:
            decision = input("-> ").lower()
            if decision in ['y', 'n']:
                break
        except:
            print("ERROR: Invalid Input. Please insert 'Y' or 'n'.")
            print("Kepp smapling with the same patient?\t Y/n")

    if decision == 'n':
        print("New patient...")
        server.operator = getMode()
    else:
        print("Same patient...")
        server.operator.label = getLabel()


def main():
    mode = getMode()
    server = Server(addr=ADDR, num_clients=NUM_CLIENTS, operator=mode)
    server.init()
    while True:
        server.start()
        server.operator = updateMode(server)


if __name__ == '__main__':
    main()
