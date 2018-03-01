import sys
import serial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.uic import loadUi


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        loadUi('OnOff_RPi_backend.ui', self)
        self.setWindowTitle('On & Off Fault Control')

    def on_btn_click(self):
        self.on_btn_clicked.connect(self.all_on)
        print("ON")

    def off_btn_click(self):
        self.off_btn_clicked.connect(self.all_off)
        print("OFF")


@pyqtSlot()
def all_on():
    api1 = 170
    api2 = 3
    api3 = 254
    ctrl = 130
    bank = 0
    csum = 45

    tx = [api1, api2, api3, ctrl, bank, csum]
    print(tx)

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


def all_off():
    api1 = 170
    api2 = 3
    api3 = 254
    ctrl = 129
    bank = 0
    csum = 44

    tx = [api1, api2, api3, ctrl, bank, csum]
    print(tx)

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


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
