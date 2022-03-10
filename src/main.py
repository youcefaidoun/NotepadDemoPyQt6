import sys
from PySide6.QtWidgets import QMainWindow, QApplication
# load ui
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
# show incons => cmd: pyside6-rcc icons.qrc -o icons.py
import icons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # connect to ui => src: https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
        ui_file_name = "ui/uimain.ui"
        ui_file = QFile(ui_file_name)

        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)

        #show ui =======================
        self.ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show(app.exec())
