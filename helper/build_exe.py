import os
import sys
# make script independent of where it is executed
cwd = os.path.join(os.path.dirname(__file__), "..")
os.chdir(cwd)

python_interpreter = sys.executable
pyinstaller = os.path.join(os.path.dirname(python_interpreter), "pyinstaller.exe")

# create .exe
os.system(f"create-version-file version.yaml --outfile gen_version_info.txt")
os.system(f"{pyinstaller} error_logging_gui.spec --noconfirm")
os.remove("gen_version_info.txt")
