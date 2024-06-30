from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class TabLearning(QWidget):
    def __init__(self):
        super().__init__()

        browser = QWebEngineView()
        html_content = open("html/index.html","r").read() + f"<style>{open("html/main.css", "r").read()}</style>" + f"<script>{open("html/main.js", "r").read()}</script>"
        browser.setHtml(html_content)
        layout = QVBoxLayout()
        layout.addWidget(browser)
        self.setLayout(layout)


class TabManagement(QWidget):
    def __init__(self):
        super().__init__()
