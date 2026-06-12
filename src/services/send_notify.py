import subprocess
import sys

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
        subprocess.run(
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
send_gdbus_notification("tite","message",None,2)