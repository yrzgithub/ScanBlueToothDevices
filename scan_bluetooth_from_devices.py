import bluetooth
from pyttsx3 import init

convertor = init()


def sayAndPrint(text):
    print(text)
    convertor.say(text)
    convertor.runAndWait()


def connect_to_bluetooth():
    sayAndPrint("Searching for available devices...")
    devices = dict(bluetooth.discover_devices(duration=1, lookup_names=True))  # increase duration
    if len(devices) == 0:
        sayAndPrint("No devices available...")
        return None
    sayAndPrint("The available devices are...")
    for i in devices:
        sayAndPrint(devices[i])
    my_device = input("Enter the wifi name").lower()  # get through voice
    bluetooth_address = None
    for i, j in zip(devices, devices.values()):
        if my_device in j.lower():
            bluetooth_address = i.lower()
            break
    print(bluetooth_address)
    bluetooth_socket = bluetooth.BluetoothSocket()
    bluetooth_socket.bind(("127.0. 0.1", 1500))
    bluetooth_socket.listen()
    bluetooth_socket.connect((bluetooth_address, 1500))
    file = open(r"C:\circuit Lab\Bonafide.pdf", "rb")
    bluetooth_socket.sendfile(file)


connect_to_bluetooth()
