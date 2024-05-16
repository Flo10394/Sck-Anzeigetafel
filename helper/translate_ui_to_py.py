import os
import sys

# make script independent of where it is executed
cwd = os.path.join(os.path.dirname(__file__), "..")
os.chdir(cwd)

executable = os.path.join(os.path.dirname(sys.executable), "pyuic5.exe")

# create .exe
os.system(f"{executable} ui/display.ui -o ui/generated_display.py")
os.system(f"{executable} ui/control.ui -o ui/generated_control.py")