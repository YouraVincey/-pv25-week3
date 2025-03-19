import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont, QColor, QPalette

class CoolMouseEventApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Mouse EH")
        self.setGeometry(100, 100, 600, 500)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#1ABC9C"))  
        self.setPalette(palette)
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.label = QLabel("", self)
        self.label.setFixedSize(10, 10)  
        self.label.setGeometry(250, 200, 10, 10)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        self.label.setStyleSheet("background-color: #E67E22; border-radius: 5px;")
        
        self.animation = QPropertyAnimation(self.label, b"geometry")
        self.animation.setDuration(500)
        
        self.show()
    
    def mouseMoveEvent(self, event):
        self.label.move(event.x() - 5, event.y() - 5)
        self.setWindowTitle(f"Koordinat Mouse: {event.x()}, {event.y()}")
    
    def enterEvent(self, event):
        new_x = random.randint(0, self.width() - self.label.width())
        new_y = random.randint(0, self.height() - self.label.height())
        self.animation.setStartValue(self.label.geometry())
        self.animation.setEndValue(QRect(new_x, new_y, 200, 50))
        self.animation.start()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoolMouseEventApp()
    window.setMouseTracking(True)
    sys.exit(app.exec_())
