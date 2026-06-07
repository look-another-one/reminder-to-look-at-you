import subprocess
import sys
from pathlib import Path
# added for not installed packages.
import importlib.util

root = Path(__file__).resolve().parent.parent.parent


is_win = None

# added detection system: 
linux_det , win_det = 'linux','win32'
if sys.platform == linux_det:
    is_win = False
    icon = root / "assets" / "alert.png" 
elif sys.platform == win_det:
    is_win = True
    icon = root / "assets" / "alert.ico"


def send_win_notification(title, message , icon ,timeout):
    """ Windows compatible fallback"""
    if importlib.util.find_spec('plyer') is None:
        subprocess.check_call(
        [sys.executable, "-m", "pip", "install", 'plyer']
        )
    else:
        print('package check done..')
        
    from plyer import notification
        
    # proper windows fallback : after check    
    notification.notify(title=title, message=message, app_icon=str(icon),timeout=timeout)
    
    return f'launched win_plyer with title: {title}'
        
    



def send_gdbus_notification(title, message, icon, timeout):
    """
    Sends a desktop notification using the standard library by breaking 
    out the parameters into distinct command line array elements.
    """
    command = [
        "gdbus", "call",
        "--session",
        "--dest", "org.freedesktop.Notifications",
        "--object-path", "/org/freedesktop/Notifications",
        "--method", "org.freedesktop.Notifications.Notify",
        "PythonApp",              
        "0",                      
        str(icon),                    
        title,                    
        message,                     
        "[]",                     
        "{}",                     
        str(timeout)
    ]
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return True
    except FileNotFoundError:
        print("Error: The 'gdbus' utility is missing from this OS.", file=sys.stderr)
        return False
    except subprocess.CalledProcessError as e:
        print(f"GDBus call failed: {e.stderr.strip()}", file=sys.stderr)
        return False
        
        
if __name__ == "__main__":
    if is_win:
        send_win_notification("Time for a break!","Look at something 20 feet away", icon, 10)
    else:
        send_gdbus_notification("Time for a break!", "Look at something 20 feet away", icon, 5000)