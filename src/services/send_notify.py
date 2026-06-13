import subprocess
import sys

def send_notification(title:str, message:str, icon:PATH, timeout:str) -> None:
    """
    Sends a desktop notification using the libnotify lib 
    """
    command = [
            "notify-send",
            title,
            message,
            "-i", 
            icon,
            "-t",
            timeout
    ]
    try:
        subprocess.run(
            command
        )
    except FileNotFoundError:
        print("Error: The 'libnotify' lib is missing from this OS.", file=sys.stderr)