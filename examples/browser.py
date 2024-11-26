import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мини-браузер")
        
        layout = QVBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Введите URL...")
        self.url_bar.returnPressed.connect(self.load_url)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        
        layout.addWidget(self.url_bar)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
