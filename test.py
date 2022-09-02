import serial


def run():
    ser = serial.Serial("/dev/ttyAMA0", 9600)
    readedText = ser.readlines()
    print(readedText)
    ser.close()


def main():
    run()


if __name__ == "__main__":
    main()
