# RECORD BUTTON GUI
import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


import pyaudio
import wave



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'QPushButton'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        # create form with number spinner
        # self.spinner()
        # mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.formGroupBox)
        # self.setLayout(mainLayout)
        
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('Record', self)
        button.setToolTip('This is an example button')
        button.move(100,70) 
        button.clicked.connect(self.recSound)
        button.setStyleSheet("background-color: #cc3a33; border: none; font-weight:bold;") 
        button.resize(100,100)
        self.show()

    # def spinner(self):
    #     self.formGroupBox = QGroupBox("")
    #     layout = QFormLayout()
    #     # layout.addRow(QLabel("Name:"), QLineEdit())
    #     # layout.addRow(QLabel("Country:"), QComboBox())
    #     spinner = QSpinBox()
    #     spinner.setValue(4)
    #     # spinner.setStyleSheet("QSpinBox { border: 3px solid red; border-radius: 5px; background-color: yellow; min-height: 150px; min-width: 150px; }")
    #     # spinner.setStyleSheet("QSpinBox { border: 3px inset grey; width:150px;} ")
    #     # spinner.setStyleSheet("QSpinBox::down-button { subcontrol-position: right; width: 40px; height: 35px;}")
    #     # spinner.setStyleSheet("QSpinBox::up-button { subcontrol-position: left; width: 40px; height: 35px;}")
    #     layout.addRow(QLabel("Time:"), spinner)
    #     self.formGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
    
    def recSound(self):
        # This records an audio file
        CHUNK = 512
        FORMAT = pyaudio.paInt16 #paInt8
        CHANNELS = 1
        RATE = 44100 #sample rate
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "rp3audio/rp3output.wav"
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) #buffer
        print("* recording")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

            data = stream.read(CHUNK)
            frames.append(data) # 2 bytes(16 bits) per channel
        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        return;
    

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())