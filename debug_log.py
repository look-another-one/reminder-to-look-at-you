import platform
import pip
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
print(pip.__version__)

# ------------ OS -----------------
print("------------------ OS ------------------")
try:
    subprocess.run(["cat","/etc/os-release"])
except: 
    print("subprocces failed!")





