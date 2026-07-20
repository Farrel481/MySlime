import sys

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QLabel, QWidget, QApplication

class Companion(QWidget):
    def __init__(self):
        super().__init__()
        self.drag_offset = None
        self.is_carried = False
        self.bob_step = 0
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint 
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(180, 180)
        self.setCursor(Qt.OpenHandCursor)
        
        self.blob = QLabel("o", parent=self)
        self.blob.setStyleSheet("""color: #8B5CF6; font-size: 130px;""")
        self.blob.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.blob.adjustSize()
        self.blob.move(24, 8)

        self.hint = QLabel("Drag me!", parent=self)
        self.hint.setStyleSheet("""color: white; font-size: 12px;""")
        self.hint.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.center_hint()
        
        self.animation_timer = QTimer(self)
        self.animation_timer.setInterval(100)
        self.animation_timer.timeout.connect(self.animate_carried)

    def center_hint(self):
        self.hint.adjustSize()
        x_position = (self.width() - self.hint.width()) // 2
        self.hint.move(x_position, 145)

    def set_carried(self, carried):
        self.is_carried = carried
        if carried:
            self.hint.setText("Hey whachu doin!")
            self.animation_timer.start()
        else:
            self.hint.setText("Drag me!")
            self.animation_timer.stop()
            self.blob.move(24, 8)

        self.center_hint()

    def animate_carried(self):
        if not self.is_carried:
            return
        self.bob_step = (self.bob_step + 1) % 2
        if self.bob_step == 0:
            self.blob.move(24, 3)
        else:
            self.blob.move(24, 8)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_offset = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )

            self.setCursor(Qt.ClosedHandCursor)
            self.is_carried = True

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drag_offset is not None:
            new_position = event.globalPosition().toPoint() - self.drag_offset
            self.move(new_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_offset = None
            self.setCursor(Qt.OpenHandCursor)
            self.is_carried = False
app = QApplication(sys.argv)
companion = Companion()
companion.show()
sys.exit(app.exec())
