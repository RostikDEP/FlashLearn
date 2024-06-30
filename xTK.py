import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class HTMLViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HTML Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        self.html_content = open("html/index.html", "r").read() + f"<style>{open("html/main.css", "r").read()}</style>" + f"<script>{open("html/main.js", "r").read()}</script>"

        self.browser.setHtml(self.html_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = HTMLViewerApp()
    viewer.show()
    sys.exit(app.exec_())
