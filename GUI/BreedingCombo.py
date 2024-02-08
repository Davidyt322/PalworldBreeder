from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
from PySide6.QtGui import QImage
import sys
import os
from main import *
from button import Button
from MessageBox import MessageBox

class BreedingCombo(QWidget):
    def __init__(self):
        super().__init__()

        self.name1_text = QLineEdit()
        self.name1_text.setStyleSheet("color: white; font-size: 16px;")
        self.name1_text.setFixedHeight(40)
        self.name2_text = QLineEdit()
        self.name2_text.setStyleSheet("color: white; font-size: 16px;")
        self.name2_text.setFixedHeight(40)
        self.button = Button("Show Images")
        self.next_button = Button("Next Image")
        self.save_button = Button("Save Image")
        self.image_label = QLabel()
        destination_label = QLabel("Destination:")
        destination_description = QLabel("Enter the name of the destination pal")
        destination_label.setStyleSheet("color: white; font-size: 20px;")
        destination_description.setStyleSheet("color: white; font-size: 16px;")
        origin_label = QLabel("Origin:")
        origin_description = QLabel("Enter the name of the origin pal")
        origin_label.setStyleSheet("color: white; font-size: 20px;")
        origin_description.setStyleSheet("color: white; font-size: 16px;")

        layout = QVBoxLayout()

        layout.addWidget(origin_label)
        layout.addWidget(origin_description)
        layout.addWidget(self.name1_text)
        layout.addWidget(destination_label)
        layout.addWidget(destination_description)
        layout.addWidget(self.name2_text)
        layout.addWidget(self.button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

        self.images = []
        self.current_image_index = 0