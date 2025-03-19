from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox)
from PyQt5.QtGui import QFont
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Week 2")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: lightgreen;")
        main_layout = QVBoxLayout()
        
        identity_group = QGroupBox("Identitas")
        identity_layout = QVBoxLayout()         
        identity_layout.addWidget(QLabel("Nama : Pradiva Wiyudha Maheswara"))
        identity_layout.addWidget(QLabel("Nim : F1D022151"))
        identity_layout.addWidget(QLabel("Kelas : D"))
        identity_group.setLayout(identity_layout)
        main_layout.addWidget(identity_group)
        
        nav_group = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)
        
        form_group = QGroupBox("User Registration")
        form_layout = QFormLayout()
        
        form_layout.addRow("Full Name:", QLineEdit())
        form_layout.addRow("Email:", QLineEdit())
        form_layout.addRow("Phone:", QLineEdit())
        
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton("Male"))
        gender_layout.addWidget(QRadioButton("Female"))
        form_layout.addRow("Gender:", gender_layout)
        
        country_combo = QComboBox()
        country_combo.addItems(["Select", "LOMBOK", "BIMA", "DOMPU", "SUMBAWA"])
        form_layout.addRow("Country:", country_combo)
        
        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)
        
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton("Submit"))
        action_layout.addWidget(QPushButton("Cancel"))
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())
