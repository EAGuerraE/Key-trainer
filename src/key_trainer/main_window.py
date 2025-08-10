from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Trainer")
        self.setMinimumSize(600, 400)  # Puedes maximizarla luego
        self.label = QLabel("A", alignment=Qt.AlignCenter)  # Placeholder
        self.setCentralWidget(self.label)
