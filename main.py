from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
from tabs import TabLearning, TabManagement
import sys

import config


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(config.TITLE)
        self.setGeometry(100, 100, 800, 650)
        self.tabs = QTabWidget(self)
        self.tabs.setStyleSheet("background-color : red")
        self.tabs.setGeometry(0, 40, 800, 600)
        self.tabs.addTab(TabLearning(), "Learning")
        self.tabs.addTab(TabManagement(), "Add Words")




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
