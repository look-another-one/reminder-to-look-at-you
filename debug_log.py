import platform
import subprocess
import os
# get system informations

print("---------- System --------------")
print(platform.system())
print(platform.machine())
print(platform.architecture())
print(platform._node())

# --------- Python Related ---------
print("---------- Python --------------")
print(platform.python_version())
print(platform.python_compiler())

# ------------ OS -----------------
print("------------------ OS ------------------")
try:
    subprocess.run(["cat","/etc/os-release"])
except: 
    print("subprocces failed!")

# ---------- Notification Manager --------
print("---------Notification Manager---------")
try:
    subprocess.run(['pgrep','-lfa','"dunst|xfce4-notifyd|gnome-shell|kdeinit|notification-daemon|mutter|swaync|mako"'])
except:
    print("notification manager check failed..")

# --------- Display Manager ------- 
print("----------Display Manager-------- ")
try: 
    subprocess.run("echo $XDG_CURRENT_DESKTOP",shell=True)
except:
    print("Display Manager check failed... ")
