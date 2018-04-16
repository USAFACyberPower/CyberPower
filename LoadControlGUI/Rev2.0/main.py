import sys
import serial
import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi


def serial_transmit(tx):
    # Uncomment the print(tx) command for transmission verification
    # tx = [api1, api2, api3, ctrl, bank, csum]
    # print(tx)
    # Establish USB Virtual Serial Connection
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1
    )
    # Uncomment the time.sleep(secs) command for wireless buffer correction
    time.sleep(0.13)
    # Send OPCODE Serial Bits (TX) to Relay Board.
    ser.write(serial.to_bytes(tx))


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.ui = loadUi('LoadControlGUI_Man.ui', self)

    # RESISTIVE LOAD SET-UP
        # Configure menu and reset buttons.
        self.btn_Unbalanced.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.btn_Balanced.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loadResetB.clicked.connect(self.btn_reset_clicked)
        self.btn_loadResetU.clicked.connect(self.btn_reset_clicked)


    @pyqtSlot()
# BEGIN MAIN MENU DEFINITIONS
    # All Locations - Master Reset
    def btn_reset_clicked(self):
        # Reset All
        tx = [170, 3, 254, 129, 0, 44]
        serial_transmit(tx)

# END MAIN MENU DEFINITIONS


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
