from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QInputDialog)
from PyQt5.QtCore import pyqtSlot, pyqtSignal
import sys
import pyaudio
import wave

class spindemo(QWidget):
   def __init__(self, parent = None):
      super(spindemo, self).__init__(parent)
      
      layout = QVBoxLayout()
      self.l1 = QLabel("current value:")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
      self.sp = QSpinBox()
		
      layout.addWidget(self.sp)
      self.sp.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")
		
   def valuechange(self):
      self.l1.setText("current value:"+str(self.sp.value()))

def main():
   app = QApplication(sys.argv)
   ex = spindemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()