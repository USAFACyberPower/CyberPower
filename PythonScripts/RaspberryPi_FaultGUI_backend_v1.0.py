import sys
import serial
from PyQt5 import QtCore, QtGui, uic


form_class = uic.loadUiType("RaspberryPi_FaultGUI_v1.0.ui")[0]
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.on_btn.clicked.connect(self.on_button_clicked)
        self.off_btn.clicked.connect(self.off_button_clicked)

    def on_btn_clicked(self):
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 130
        bank = 0
        csum = 45

        tx = [api1, api2, api3, ctrl, bank, csum]

        # Establish USB Virtual Serial Connection
        ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        )
        # Send OPCODE Serial Bits (TX) to Relay Board.
        ser.write(serial.to_bytes(tx))


    def off_btn_clicked(self):
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 0
        csum = 44

        tx = [api1, api2, api3, ctrl, bank, csum]

        # Establish USB Virtual Serial Connection
        ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        )
        # Send OPCODE Serial Bits (TX) to Relay Board.
        ser.write(serial.to_bytes(tx))


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()