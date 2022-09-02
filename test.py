import serial
import time


def run():
    ser = serial.Serial("/dev/ttyAMA0", 9600)
    return ser.readlines()


def main():
    print("Start")
    while True:

        print("Reveived: ".run())


if __name__ == "__main__":
    main()
