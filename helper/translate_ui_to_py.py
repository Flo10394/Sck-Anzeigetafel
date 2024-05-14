import os
import sys

# make script independent of where it is executed
cwd = os.path.join(os.path.dirname(__file__), "..")
os.chdir(cwd)

executable = os.path.join(os.path.dirname(sys.executable), "pyuic5.exe")

# create .exe
os.system(f"{executable} ui/display.ui -o ui/generated_display.py")
os.system(f"{executable} ui/control.ui -o ui/generated_control.py")

with open("ui/generated_display.py", "a") as f:
    f.write("""    
if __name__ == "__main__":
    from PyQt5 import QtWidgets


    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)


    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
    """)