from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QInputDialog)
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from functools import partial
import sys
import pyaudio
import wave
 
class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.newTime = 4
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        # mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Record for time")
 
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("")
        layout = QFormLayout()
        # SPINNER STUFF
        spinner = QSpinBox()
        spinner.setStyleSheet("QSpinBox { border: 3px inset grey; width:100px; height:50px;} QSpinBox::up-button { subcontrol-position: left; width: 40px; height: 35px;}  QSpinBox::down-button { subcontrol-position: right; width: 40px; height: 35px;}")
        spinner.setValue(4)
        print("Seconds:", spinner.value())
        spinner.valueChanged.connect(self.secondsChange)

        layout.addRow(QLabel("Sec:"), spinner)        
        #Need to get the value of the spinner to recSound
        # BUTTON STUFF
        button = QPushButton('Record')
        button.clicked.connect(self.recSound)
        button.setStyleSheet("background-color: #cc3a33; border: none; font-weight:bold; height:100px;") 
        layout.addRow(button)
        self.formGroupBox.setLayout(layout)

    # @pyqtSlot(int)
    def secondsChange(self, value):
        print("Seconds:", value)
        self.newTime = value

    # @pyqtSlot()
    def recSound(self):
        # This records an audio file
        CHUNK = 512
        FORMAT = pyaudio.paInt16 #paInt8
        CHANNELS = 1
        RATE = 44100 #sample rate
        RECORD_SECONDS = self.newTime #this is where the variable for seconds should live from the spinbox
        WAVE_OUTPUT_FILENAME = "rp3audio/rp3output.wav"
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) #buffer
        print("* Recording for ", self.newTime)
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
    dialog = Dialog()
sys.exit(dialog.exec_())
