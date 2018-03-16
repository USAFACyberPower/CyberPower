import sys
import serial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi


def serial_transmit(tx):
    # Print the opcode for transmission verification
    # tx = [api1, api2, api3, ctrl, bank, csum]
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


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.ui = loadUi('FaultControlGUI.ui', self)

        # Main menu functions
        self.ui.stackedWidget.setCurrentIndex(0)
        self.btn_OneLine_loc1TL1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.btn_OneLine_loc2TL5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.btn_OneLine_loc3TL4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.btn_OneLine_loc4TL7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.btn_OneLine_loc5TL9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.btn_OneLine_loc6TL6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))

        # Fault Location 1 Functions
        self.btn_OneLine_loc1TL1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.btn_loc1_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc1_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 2 Functions
        self.btn_OneLine_loc2TL5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.btn_loc2_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc2_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 3 Functions
        self.btn_OneLine_loc1TL1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.btn_loc3_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc3_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 4 Functions
        self.btn_OneLine_loc2TL5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.btn_loc4_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc4_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 5 Functions
        self.btn_OneLine_loc1TL1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.btn_loc5_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc5_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 6 Functions
        self.btn_OneLine_loc2TL5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        self.btn_loc6_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc6_reset.clicked.connect(self.btn_reset_clicked)

    @pyqtSlot()
    def btn_reset_clicked(self):
        tx = [170, 3, 254, 129, 0, 44]
        serial_transmit(tx)


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
