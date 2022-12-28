import os
import random
import time

from PyQt5 import QtCore, QtGui, QtWidgets

class Viewbot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Create a list of video links from a .txt file
        with open('video_links.txt', 'r') as f:
            self.video_links = f.readlines()
        
        # Set the interval between videos to a random value between 10 and 20 seconds
        self.interval = random.uniform(10, 20)
        
        # Set up the GUI
        self.initUI()
        
    def initUI(self):
        # Create a label to display the current video link
        self.link_label = QtWidgets.QLabel('Current Video Link:', self)
        
        # Create a label to display the elapsed time
        self.time_label = QtWidgets.QLabel('Elapsed Time:', self)
        
        # Create a slider to adjust the interval between videos
        self.interval_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.interval_slider.setMinimum(10)
        self.interval_slider.setMaximum(20)
        self.interval_slider.setValue(self.interval)
        self.interval_slider.valueChanged.connect(self.setInterval)
        
        # Create a button to start and stop the viewbot
        self.start_button = QtWidgets.QPushButton('Start', self)
        self.start_button.clicked.connect(self.start)
        
        # Set up the layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.link_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.interval_slider)
        layout.addWidget(self.start_button)
        
        self.setLayout(layout)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Viewbot')
        self.show()
        
    def setInterval(self):
        # Update the interval when the slider is moved
        self.interval = self.interval_slider.value()
        
    def start(self):
        # Start the viewbot loop
        self.viewbot_thread = QtCore.QThread()
        self.viewbot_thread.run = self.viewbotLoop
        self.viewbot_thread.start()
        
    def viewbotLoop(self):
        # Continuously play videos from the list
        while True:
