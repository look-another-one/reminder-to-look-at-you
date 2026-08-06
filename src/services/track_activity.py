import socket
import os 
import json
import logging

logger = logging.getLogger(__name__)

class TrackScreenTime:
    def __init__(self):
        self.registery = {}
        self.focused_window = None
        self.check_window_manager()

    def check_window_manager(self):
        '''
        Check window manager if not get raise a valueerror
        '''
        if not os.getenv("NIRI_SOCKET"):
            logger.error("no NIRI_SOCKET env found")
            raise ValueError("niri socket not found")
        logger.info("window manager checked passed")
    
    def connect_to_window_manager(self):
        '''
        Connect with window manager and stream niri ipc output
        '''
        sock_path = os.environ["NIRI_SOCKET"]
        logger.info("connecting to window manager")
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
            s.connect(sock_path)
            request = (json.dumps("EventStream") + "\n").encode()
            s.sendall(request)
            
            file = s.makefile("r")
            for line in file:
                output = json.loads(line.strip())
                
                if "WindowFocusChanged" in output:
                    self.window_focus_changed(output["WindowFocusChanged"])
                elif "WindowOpenedOrChanged" in output:
                    self.window_opened(output["WindowOpenedOrChanged"])
                elif "WindowClosed" in output:
                    self.window_closed(output["WindowClosed"])

    def window_opened(self, event_data):
        window_info = event_data.get("window", {})
        app_id = window_info.get("app_id")
        window_id = window_info.get("id")
        
        logger.debug(f"window opened {app_id},{window_id}")
        
        if not app_id or not window_id:
            return

        if app_id not in self.registery:
            self.registery[app_id] = [window_id]
        elif window_id not in self.registery[app_id]:
            self.registery[app_id].append(window_id)
    
    def window_focus_changed(self, event_data):
        window_id = event_data.get("id")
        logger.debug(f"window opened {window_id}")
        self.focused_window = window_id

    def window_closed(self, event_data):
        window_id = event_data.get("id")
        logger.debug(f"window closed {window_id}",)
        if not window_id:
            return

        for app_id, id_list in list(self.registery.items()):
            if window_id in id_list:
                id_list.remove(window_id)
                
                if not id_list:
                    del self.registery[app_id]
                
                break
        
        if self.focused_window == window_id:
            self.focused_window = None