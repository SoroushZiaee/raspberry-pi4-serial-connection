import socket
from tkinter import SEPARATOR
import tqdm
import os

SEPARATOR = "/"
BUFFER_SIZE = 4096

host = "localhost"
port = 5001

filename = "dataset.csv"

filesize = os.path.getsize(os.path.join("data", filename))

print(f"{filesize}")

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
