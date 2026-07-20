import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget

class Companion(QWidget):
    def __init__(self):
        super().__init__()
        self.drag_offset = None
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint 
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(180, 180)
        self.setCursor(Qt.OpenHandCursor)
        
        blob = QLabel("o", parent=self)
        blob.setStyleSheet("""color: #8B5CF6; font-size: 130px;""")
        blob.setAttribute(Qt.WA_TransparentForMouseEvents)
        blob.adjustSize()
        blob.move(24, 8)

        hint = QLabel("Drag me!", parent=self)
        hint.setStyleSheet("""color: white; font-size: 12px;""")
        hint.setAttribute(Qt.WA_TransparentForMouseEvents)
        hint.adjustSize()
        hint.move(58, 145)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_offset = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )

            self.setCursor(Qt.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drag_offset is not None:
            new_position = event.globalPosition().toPoint() - self.drag_offset
            self.move(new_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_offset = None
            self.setCursor(Qt.OpenHandCursor)

app = QApplication(sys.argv)
companion = Companion()
companion.show()
sys.exit(app.exec())
