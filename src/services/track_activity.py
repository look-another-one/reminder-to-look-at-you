import socket
import os 
import json

def track_window():
    '''
    Connect to NIRI_SOCKET and get live EventStream Ouput
    '''
    sock = os.environ["NIRI_SOCKET"]
    with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as s:
        s.connect(sock)
        request = (json.dumps("EventStream") + "\n").encode()
        s.sendall(request)
        file = s.makefile("r")
        for line in file:
            output = json.loads(line.strip())
            if "WindowFocusChanged" in output.keys():
                print(f"Focused Changed to {output["WindowFocusChanged"]["id"]}")
            if "WindowOpenedOrChanged" in output.keys():
                print(f"Window Opened, Title: {output["WindowOpenedOrChanged"]["window"]["title"]}")
                print(f"Window Opened, ID: {output["WindowOpenedOrChanged"]["window"]["id"]}")
                print(f"Window Opened, APP_ID: {output["WindowOpenedOrChanged"]["window"]["app_id"]}")
            if "WindowClosed" in output.keys():
                print(f"WIndow Closed ID: {output["WindowClosed"]["id"]}")
            else:
                pass

if os.getenv("NIRI_SOCKET"):
    track_window()
else:
    print("Are You Running Inside Niri?")