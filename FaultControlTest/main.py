import sys
import serial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        loadUi('FaultControlTest_v1.0.ui', self)
        self.on_off_btn.clicked.connect(self.on_off_btn_click)

    @pyqtSlot()
    def on_off_btn_click(self):
        status = 'OFF'
        if status == 'OFF':
            # If the switch is OFF, turn it ON!
            api1 = 170
            api2 = 3
            api3 = 254
            ctrl = 130
            bank = 0
            csum = 45
            status = 'OFF'

        elif status == 'ON':
            # If the switch is ON, turn it OFF!
            api1 = 170
            api2 = 3
            api3 = 254
            ctrl = 129
            bank = 0
            csum = 44
            status = 'ON'

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
