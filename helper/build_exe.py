import os
import sys
# make script independent of where it is executed
cwd = os.path.join(os.path.dirname(__file__), "..")
os.chdir(cwd)

python_interpreter = sys.executable
pyinstaller = os.path.join(os.path.dirname(python_interpreter), "pyinstaller.exe")

create_version_file = os.path.dirname(python_interpreter) + '/create-version-file.exe'

# create .exe
os.system(f"{create_version_file} version.yaml --outfile gen_version_info.txt")
os.system(f"{pyinstaller} sck_screen.spec --noconfirm")
os.remove("gen_version_info.txt")
