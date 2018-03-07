import sys
import serial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi


def serial_transmit(tx):
    # Print the opcode for transmission verification
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
        self.ui = loadUi('FaultBankRelayCtrl.ui', self)
        self.menu_btn_all_on.clicked.connect(self.menu_btn_all_on_clicked)
        self.menu_btn_reset.clicked.connect(self.menu_btn_reset_clicked)
        # Start with the GUI main menu
        self.ui.stackedWidget.setCurrentIndex(0)
        # Bolted Fault menu functions
        self.menu_btn_bolted.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.bolted_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        # Phase AB menu functions
        self.menu_btn_phaseAB.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.phaseAB_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        # Phase AC menu functions
        self.menu_btn_phaseAC.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.phaseAC_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        # Phase BC menu functions
        self.menu_btn_phaseBC.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.phaseBC_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

    @pyqtSlot()
    def menu_btn_all_on_clicked(self):
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 130
        bank = 0
        csum = 45
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def menu_btn_reset_clicked(self):
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 0
        csum = 44
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
