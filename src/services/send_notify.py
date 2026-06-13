import subprocess
import sys
from src.utils.icons import alert,water_bottle

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

send_notification("TIelec","mes",water_bottle,"5000")