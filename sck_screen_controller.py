import sys
import os
import pickle
import argparse
import time
from enum import Enum, auto
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal as QSignal
from PyQt5.QtCore import QSize, QPoint, Qt
from PyQt5.QtGui import QScreen, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsPixmapItem, QLabel, QWidget, QFileDialog

from ui.generated_display import Ui_Display
from ui.generated_control import Ui_ControlWindow


def is_exe():
    return getattr(sys, 'frozen', False)


class AppData:
    class Display:
        def __init__(self):
            self.x = 0
            self.y = 0

    class Emblem:
        def __init__(self):
            self.home = "static/wappen_sck.png"
            self.guest = "static/wappen_jechtingen.jpg"

    def __init__(self):
        self.display = self.Display()
        self.emblem = self.Emblem()


class AppDataHandler:
    DEFAULT_APP_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "app_data.pkl"))

    def __init__(self, app_data_path: str or None = None):
        if app_data_path is None:
            self.app_data_path = self.DEFAULT_APP_DATA_PATH
        else:
            self.app_data_path = app_data_path

        if not os.path.exists(self.app_data_path):
            self._create_default_app_data()

        self._load_app_data()

    def _create_default_app_data(self):
        default_app_data = AppData()
        with open(self.app_data_path, "wb") as f:
            pickle.dump(default_app_data, f)

    def _load_app_data(self):
        with open(self.app_data_path, "rb") as f:
            self.app_data = pickle.load(f)
        print("loaded app data")

    def store_app_data(self):
        with open(self.app_data_path, "wb") as f:
            pickle.dump(self.app_data, f)
        print("Stored app data")


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
        self.seconds_elapsed = 0
        self.is_second_half: bool = False

    def reset(self):
        self.seconds_elapsed = 0
        self._set_new_time()

    def resume(self):
        self.status = self.Status.RUNNING
        print("start")

    def pause(self):
        self.status = self.Status.PAUSED
        print("pause")

    def set_elapsed_time(self, minutes: int, seconds: int):
        self.seconds_elapsed = minutes * 60 + seconds
        if minutes <= 45:
            self.is_second_half = False
        else:
            self.is_second_half = True
        self._set_new_time()

    def _set_new_time(self):
        minutes = int(self.seconds_elapsed // 60)
        seconds = int(self.seconds_elapsed) % 60
        formatted_time = f"{minutes:02}:{seconds:02}"
        self.time_label.setText(formatted_time)

    def handle_auto_stop(self):
        if self.is_second_half:
            if self.seconds_elapsed >= 90*60:
                print("Auto stop second half")
                self.pause()
        else:
            if self.seconds_elapsed >= 45*60:
                print("Auto stop first half")
                self.pause()
                self.is_second_half = True

    def run(self):
        while True:
            t_start = time.time()
            time.sleep(0.1)
            if self.status == self.Status.RUNNING:
                self.seconds_elapsed += time.time() - t_start
                self.handle_auto_stop()
                self._set_new_time()

            elif self.status == self.Status.PAUSED:
                pass




class DisplayWindow(QWidget, Ui_Display):

    def __init__(self, screen: QScreen, app_data_handler: AppDataHandler):
        super().__init__()
        self.setupUi(self)
        self.app_data_handler: AppDataHandler = app_data_handler
        self.app_data: AppData = self.app_data_handler.app_data
        self.screen: QScreen = screen

        # constants
        self.background_color = "black"
        self.text_color = "white"

        # get original position and width data
        self.graphic_wappen_heim_geometry = self.graphic_wappen_heim.geometry()
        self.graphic_wappen_gast_geometry = self.graphic_wappen_gast.geometry()

        self.set_window_properties()
        self.set_background_image()
        self.init_from_app_data()

    def init_from_app_data(self):
        for path, function in zip([self.app_data.emblem.home, self.app_data.emblem.guest], [self.set_home_image, self.set_guest_image]):
            if isinstance(path, str) and os.path.exists(path):
                function(path)

    def window_position_changed(self):
        self.move(QPoint(self.app_data.display.x, self.app_data.display.y))

    def set_window_properties(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # no window title
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # always on top

        text_properties = [self.label_spielstand_heim,
                           self.label_spielstand_gast,
                           self.label_time,
                           self.label_spielstand_doppelpunkt,
                           self.graphic_wappen_gast,
                           self.graphic_wappen_heim]

        [self._set_item_properties(item=item) for item in text_properties]

    def _set_item_properties(self, item):
        stylesheet = f"""
            background: transparent;
            color: {self.text_color};
        """

        item.setStyleSheet(stylesheet)

    def set_background_image(self):
        background_path = os.path.abspath("static/hintergrund_1.jpg")
        image_pixmap = QPixmap(background_path)
        scaled_pixmap = image_pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

    def _set_image(self, graphics_object, image_path: str):
        scene = QGraphicsScene()
        pixmap = QPixmap(image_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        graphics_object.setScene(scene)
        graphics_object.fitInView(scene.sceneRect())

    def set_home_image(self, image_path: str):
        self._set_image(graphics_object=self.graphic_wappen_heim, image_path=image_path)

    def set_guest_image(self, image_path: str):
        self._set_image(graphics_object=self.graphic_wappen_gast, image_path=image_path)


class MainControlWindow(QtWidgets.QMainWindow, Ui_ControlWindow):
    worker_time_signals = WorkerTimeSignals()

    def __init__(self, application: QtWidgets.QApplication, parsed_args):
        super().__init__()
        self.setupUi(self)
        self.application = application
        self.parsed_args = parsed_args
        self.is_exe = is_exe()

        self.app_data_handler: AppDataHandler = AppDataHandler()
        self.app_data: AppData = self.app_data_handler.app_data
        self.init_from_app_data()

        # objects
        self.display_window = DisplayWindow(app_data_handler=self.app_data_handler,
                                            screen=self.application.primaryScreen())

        self.display_window.show()

        # threads
        self.threadPool = QtCore.QThreadPool()
        self.worker_time = WorkerTime(time_label=self.display_window.label_time, signals=self.worker_time_signals)
        self.threadPool.start(self.worker_time)

        for item in [self.line_edit_display_pos_x, self.line_edit_display_pos_y]:
            item.textChanged.connect(self.display_position_edited)

        self.button_time_start.pressed.connect(self.worker_time.resume)
        self.button_time_pause.pressed.connect(self.worker_time.pause)
        self.button_time_reset.pressed.connect(self.worker_time.reset)
        self.button_time_manual.pressed.connect(self.set_elapsed_time)

        self.button_score_home_plus.pressed.connect(lambda: self.button_score_home_clicked(True))
        self.button_score_home_minus.pressed.connect(lambda: self.button_score_home_clicked(False))

        self.button_score_guest_plus.pressed.connect(lambda: self.button_score_guest_clicked(True))
        self.button_score_guest_minus.pressed.connect(lambda: self.button_score_guest_clicked(False))

        self.button_select_emblem_home.pressed.connect(self.button_select_emblem_home_clicked)
        self.button_select_emblem_guest.pressed.connect(self.button_select_emblem_guest_clicked)

        self.display_position_edited()

    def init_from_app_data(self):
        self.line_edit_display_pos_x.setText(str(self.app_data_handler.app_data.display.x))
        self.line_edit_display_pos_y.setText(str(self.app_data_handler.app_data.display.y))

    # CALLBACK FUNCTIONS #

    def display_position_edited(self):
        try:
            self.app_data_handler.app_data.display.x = int(self.line_edit_display_pos_x.text())
            self.app_data_handler.app_data.display.y = int(self.line_edit_display_pos_y.text())
            self.app_data_handler.store_app_data()
            self.display_window.window_position_changed()
        except:
            pass

    def _handle_score_click(self, item: QLabel, is_plus: bool):
        score = int(item.text())
        if is_plus:
            score += 1
        else:
            score -= 1

        score = max(score, 0)

        item.setText(str(score))

    def button_score_home_clicked(self, is_plus: bool):
        self._handle_score_click(item=self.display_window.label_spielstand_heim, is_plus=is_plus)

    def button_score_guest_clicked(self, is_plus: bool):
        self._handle_score_click(item=self.display_window.label_spielstand_gast, is_plus=is_plus)


    def button_select_emblem_home_clicked(self):
        file_path = self.openFileDialog()
        if file_path:
            self.app_data.emblem.home = file_path
            self.display_window.set_home_image(image_path=self.app_data.emblem.home)
            self.app_data_handler.store_app_data()


    def button_select_emblem_guest_clicked(self):
        file_path = self.openFileDialog()
        if file_path:
            self.app_data.emblem.guest = file_path
            self.display_window.set_guest_image(image_path=self.app_data.emblem.guest)
            self.app_data_handler.store_app_data()


    def set_elapsed_time(self):
        minutes = int(self.line_edit_time_manual_minutes.text())
        seconds = int(self.line_edit_time_manual_seconds.text())
        self.worker_time.set_elapsed_time(minutes=minutes, seconds=seconds)


    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Bilddatei auswählen", "", "All Files (*);", options=options)
        return file_path



if __name__ == "__main__":
    app = QApplication(sys.argv)

    parser = argparse.ArgumentParser(prog='SCK Anzeigetafel', description='Tool für SCK Anzeigetafel')
    args = parser.parse_known_args()[0]

    w_display = MainControlWindow(application=app, parsed_args=args)
    w_display.show()

    app.exec()
