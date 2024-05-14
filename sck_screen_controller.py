import shutil
import sys
import os
import json
import traceback
import argparse
import time
from datetime import datetime
from enum import Enum, auto
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal as QSignal, QObject
from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtGui import QScreen, QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsPixmapItem, QLabel, QWidget

from ui.generated_display import Ui_MainWindow as DisplayWindow
from ui.generated_control import Ui_ControlWidget as ControlWindow

APP_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "app_data.json"))


def is_exe():
    return getattr(sys, 'frozen', False)


def create_default_app_data():
    default_app_data = {
        "dummy": 0
    }
    with open(APP_DATA_PATH, "w") as f:
        json.dump(default_app_data, f, indent=4)


def get_app_data_attribute(key: str):
    with open(APP_DATA_PATH, "r") as f:
        app_data = json.load(f)
        return app_data[key]


def set_app_data_attribute(key: str, value):
    with open(APP_DATA_PATH, "r") as f:
        app_data = json.load(f)
        app_data[key] = value
    with open(APP_DATA_PATH, "w") as f:
        json.dump(app_data, f, indent=4)


class WorkerTimeSignals:
    reset_signal = QSignal()
    pause_signal = QSignal()
    resume_signal = QSignal()


class WorkerTime(QtCore.QRunnable):

    class Status(Enum):
        PAUSED = auto()
        RUNNING = auto()

    def __init__(self, time_label: QLabel, signals: WorkerTimeSignals):
        QtCore.QRunnable.__init__(self)
        self.signals = signals
        self.time_label: QLabel = time_label
        self.status = self.Status.PAUSED
        self.time_elapsed = 0

    def reset(self):
        self.time_elapsed = 0
        self._set_new_time()

    def resume(self):
        self.status = self.Status.RUNNING
        print("start")

    def pause(self):
        self.status = self.Status.PAUSED
        print("pause")

    def _set_new_time(self):
        minutes = int(self.time_elapsed // 60)
        seconds = int(self.time_elapsed) % 60
        formatted_time = f"{minutes:02}:{seconds:02}"
        self.time_label.setText(formatted_time)

    def run(self):
        while True:
            t_start = time.time()
            time.sleep(0.1)
            if self.status == self.Status.RUNNING:
                self.time_elapsed += time.time() - t_start
                self._set_new_time()
            elif self.status == self.Status.PAUSED:
                pass




class WorkerSignals(QtCore.QObject):
    finished: QSignal = QSignal()
    error: QSignal = QSignal(tuple)
    result: QSignal = QSignal(object)
    progress: QSignal = QSignal(int)


class Worker(QtCore.QRunnable):
    def __init__(self, fn, signals, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = signals
        self.setAutoDelete(True)

    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class MainDisplayWindow(QtWidgets.QMainWindow, DisplayWindow):

    worker_time_signals = WorkerTimeSignals()

    def __init__(self, application: QtWidgets.QApplication, parsed_args):
        super().__init__()
        self.application = application
        self.parsed_args = parsed_args
        self.is_exe = is_exe()
        self.setupUi(self)

        # constants
        self.background_color = "black"
        self.text_color = "white"

        # variables

        self.screen: QScreen = self.application.primaryScreen()
        self.original_window_geometry = self.size()

        self.window_position_on_screen: QPoint = QPoint(0, 0)
        self.window_width_on_screen: QSize = QSize(0, 0)
        self.window_scaling_factor: tuple[float, float] = (1.0, 1.0)

        self.scale_window_on_screen()
        self.set_window_properties()

        self.set_home_image(image_path=r"C:\Users\spricfl\Desktop\home.png")
        self.set_gast_image(image_path=r"C:\Users\spricfl\Desktop\gast.jpg")

        if not os.path.exists(APP_DATA_PATH):
            create_default_app_data()
            print("Created default app data")
        else:
            print("Loaded app data")

        # other stuff
        self.threadPool = QtCore.QThreadPool()
        self.worker_time = WorkerTime(time_label=self.label_time, signals=self.worker_time_signals)
        self.threadPool.start(self.worker_time)

        # objects
        self.control_window = MainControlWindow(self)
        self.control_window.show()



    def scale_window_on_screen(self):
        self.window_position_on_screen = QPoint(int(self.screen.size().width() * self.parsed_args.x),
                                                int(self.screen.size().height() * self.parsed_args.y))
        self.window_width_on_screen = QSize(int(self.screen.size().width() * self.parsed_args.w),
                                            int(self.screen.size().height() * self.parsed_args.h)
                                            )

        self.window_scaling_factor = (
            self.window_width_on_screen.width() / self.original_window_geometry.width(),
            self.window_width_on_screen.height() / self.original_window_geometry.height()
        )

        self.move(self.window_position_on_screen)
        self._set_window_size()

    def _set_window_size(self):
        self.setFixedSize(self.window_width_on_screen)

    def set_window_properties(self):
        # Remove the window title bar to prevent dragging
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        # Set the window to be always on top
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.setStyleSheet(f"background-color: {self.background_color};")

        text_properties = [self.label_spielstand_heim,
                           self.label_spielstand_gast,
                           self.label_time,
                           self.label_versus,
                           self.label_spielstand_doppelpunkt]

        [self._set_text_properties(item=item) for item in text_properties]

    def _set_text_properties(self, item):
        item.setStyleSheet(f"background-color: {self.background_color}; color: {self.text_color};")

    def set_image(self, graphics_object, image_path: str):
        scene = QGraphicsScene()
        pixmap = QPixmap(image_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        graphics_object.setScene(scene)
        graphics_object.fitInView(scene.sceneRect())

    def set_home_image(self, image_path: str):
        self.set_image(graphics_object=self.graphic_wappen_heim, image_path=image_path)

    def set_gast_image(self, image_path: str):
        self.set_image(graphics_object=self.graphic_wappen_gast, image_path=image_path)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        pass

    def _on_action_exit(self):
        self.close()


class MainControlWindow(QWidget, ControlWindow):
    def __init__(self, display_window: MainDisplayWindow):
        super().__init__()
        self.setupUi(self)

        self.display_window = display_window

        self.button_time_start.pressed.connect(self.display_window.worker_time.resume)
        self.button_time_pause.pressed.connect(self.display_window.worker_time.pause)
        self.button_time_reset.pressed.connect(self.display_window.worker_time.reset)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    parser = argparse.ArgumentParser(prog='SCK Anzeigetafel', description='Tool für SCK Anzeigetafel')
    parser.add_argument("--x", dest="x", help="x-position Anzeige 0.0 - 1.0", default=0.5, type=float)
    parser.add_argument("--y", dest="y", help="y-position Anzeige 0.0 - 1.0", default=0.5, type=float)
    parser.add_argument("--w", dest="w", help="w-position Anzeige 0.0 - 1.0", default=0.5, type=float)
    parser.add_argument("--h", dest="h", help="h-position Anzeige 0.0 - 1.0", default=0.5, type=float)
    args = parser.parse_known_args()[0]

    w_display = MainDisplayWindow(application=app, parsed_args=args)
    w_display.show()

    app.exec()
