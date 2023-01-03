from fall_prevention_server import Server
from fall_prevention_modes import CollectMode, PredMode


NUM_CLIENTS = 1
PORT = 13380
IP = "192.168.6.232"
ADDR = (IP, PORT)

def getLabel():
    print("Choose Label (by the index):\n")
    print("0. Laying Center")
    print("1. Laying Left")
    print("2. Laying Right")
    print("3. Alarm Left")
    print("4. Alarm Right")
    label = input("-> ")

    if label not in ["0", "1", "2", "3", "4"]:
        return None
    
    return int(label)

def getMode():
    label = getLabel()
    if label is None:
        return None

    return CollectMode(verbose=True, label=label)

def main():
    mode = getMode()
    if mode is None:
        print("Invalid Argument!")
        return

    server = Server(addr=ADDR, num_clients=NUM_CLIENTS, operator=mode)
    server.init()
    while True:
        server.start()
        server.operator = getMode()

if __name__ == '__main__':
    main()