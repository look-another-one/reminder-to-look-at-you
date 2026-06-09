import socket
import os 
import json

def track_window():
    sock = os.environ["NIRI_SOCKET"]
    with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as s:
        s.connect(sock)
        request = (json.dumps("EventStream") + "\n").encode()
        s.sendall(request)
        file = s.makefile("r")
        for line in file:
            print(line.strip())

if os.getenv("NIRI_SOCKET"):
    track_window()
else:
    print("Are You Running Inside Niri?")