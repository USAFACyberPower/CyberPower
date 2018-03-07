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
        self.ui = loadUi('FaultBankRelayCtrl.ui', self)

        # Main menu functions
        self.ui.stackedWidget.setCurrentIndex(0)
        self.menu_btn_all_on.clicked.connect(self.menu_btn_all_on_clicked)
        self.menu_btn_reset.clicked.connect(self.menu_btn_reset_clicked)

        # Bolted Fault menu functions
        self.menu_btn_bolted.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.bolted_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.bolted_btn_reset.clicked.connect(self.menu_btn_reset_clicked)
        self.bolted_btn_relay1.clicked.connect(self.bolted_btn_relay1_clicked)
        self.bolted_btn_relay2.clicked.connect(self.bolted_btn_relay2_clicked)
        self.bolted_btn_relay3.clicked.connect(self.bolted_btn_relay3_clicked)
        self.bolted_btn_relay4.clicked.connect(self.bolted_btn_relay4_clicked)
        self.bolted_btn_relay5.clicked.connect(self.bolted_btn_relay5_clicked)
        self.bolted_btn_relay6.clicked.connect(self.bolted_btn_relay6_clicked)
        self.bolted_btn_relay7.clicked.connect(self.bolted_btn_relay7_clicked)
        self.bolted_btn_relay8.clicked.connect(self.bolted_btn_relay8_clicked)

        # Phase AB menu functions
        self.menu_btn_phaseAB.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.phaseAB_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.phaseAB_btn_reset.clicked.connect(self.menu_btn_reset_clicked)
        self.phaseAB_btn_relay1.clicked.connect(self.phaseAB_btn_relay1_clicked)
        self.phaseAB_btn_relay2.clicked.connect(self.phaseAB_btn_relay2_clicked)
        self.phaseAB_btn_relay3.clicked.connect(self.phaseAB_btn_relay3_clicked)
        self.phaseAB_btn_relay4.clicked.connect(self.phaseAB_btn_relay4_clicked)
        self.phaseAB_btn_relay5.clicked.connect(self.phaseAB_btn_relay5_clicked)
        self.phaseAB_btn_relay6.clicked.connect(self.phaseAB_btn_relay6_clicked)
        self.phaseAB_btn_relay7.clicked.connect(self.phaseAB_btn_relay7_clicked)
        self.phaseAB_btn_relay8.clicked.connect(self.phaseAB_btn_relay8_clicked)

        # Phase AC menu functions
        self.menu_btn_phaseAC.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.phaseAC_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.phaseAC_btn_reset.clicked.connect(self.menu_btn_reset_clicked)

        # Phase BC menu functions
        self.menu_btn_phaseBC.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.phaseBC_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.phaseBC_btn_reset.clicked.connect(self.menu_btn_reset_clicked)


    @pyqtSlot()
    def menu_btn_all_on_clicked(self):
        tx = [170, 3, 254, 130, 0, 45]
        serial_transmit(tx)

    def menu_btn_reset_clicked(self):
        tx = [170, 3, 254, 129, 0, 44]
        serial_transmit(tx)

    # BEGIN Bolted Fault Definitions
    def bolted_btn_relay1_clicked(self):
        # Turn on relay 1 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 108, 0, 23]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)

    def bolted_btn_relay2_clicked(self):
        # Turn on relay 2 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 109, 0, 24]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)

    def bolted_btn_relay3_clicked(self):
        # Turn on relay 3 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 110, 0, 25]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)

    def bolted_btn_relay4_clicked(self):
        # Turn on relay 4 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 111, 0, 26]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)

    def bolted_btn_relay5_clicked(self):
        # Turn on relay 5 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 112, 0, 27]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)

    def bolted_btn_relay6_clicked(self):
        # Turn on relay 6 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 113, 0, 28]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)

    def bolted_btn_relay7_clicked(self):
        # Turn on relay 7 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 114, 0, 29]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)

    def bolted_btn_relay8_clicked(self):
        # Turn on relay 8 for all banks (all phases and resistor bank)
        tx = [170, 3, 254, 115, 0, 30]
        serial_transmit(tx)
        # Turn off all relays for bank 2 (resistor bank)
        tx = [170, 3, 254, 129, 2, 46]
        serial_transmit(tx)
    # END Bolted Fault Definitions

    # BEGIN Phase A/B Definitions
    def phaseAB_btn_relay1_clicked(self):
        # Turn on relay 1 for bank 1
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)
        # Turn on relay 1 for bank 3
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)

    def phaseAB_btn_relay2_clicked(self):
        # Turn on relay 2 for bank 1
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)
        # Turn on relay 2 for bank 3
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)

    def phaseAB_btn_relay3_clicked(self):
        # Turn on relay 3 for bank 1
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)
        # Turn on relay 3 for bank 3
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)

    def phaseAB_btn_relay4_clicked(self):
        # Turn on relay 4 for bank 1
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)
        # Turn on relay 4 for bank 3
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)

    def phaseAB_btn_relay5_clicked(self):
        # Turn on relay 5 for bank 1
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)
        # Turn on relay 5 for bank 3
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)

    def phaseAB_btn_relay6_clicked(self):
        # Turn on relay 6 for bank 1
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)
        # Turn on relay 6 for bank 3
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)

    def phaseAB_btn_relay7_clicked(self):
        # Turn on relay 7 for bank 1
        tx = [170, 3, 254, 114, 1, 30]
        serial_transmit(tx)
        # Turn on relay 7 for bank 3
        tx = [170, 3, 254, 114, 3, 32]
        serial_transmit(tx)

    def phaseAB_btn_relay8_clicked(self):
        # Turn on relay 8 for bank 1
        tx = [170, 3, 254, 115, 1, 31]
        serial_transmit(tx)
        # Turn on relay 8 for bank 3
        tx = [170, 3, 254, 115, 3, 33]
        serial_transmit(tx)


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
