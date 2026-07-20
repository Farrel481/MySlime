import sys
from PySide6.QtWidgets import QApplication
from companion_widget.py import Companion

def main():
    app = QApplication(sys.argv)
    companion = Companion()
    companion.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

