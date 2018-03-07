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

        # GUI main menu
        self.ui.stackedWidget.setCurrentIndex(0)
        # Master Fault Button
        self.menu_btn_all_on.clicked.connect(self.menu_btn_all_on_clicked)
        # Master Reset Button
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

    def bolted_btn_relay1_clicked(self):
        # Turn on relay 1 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 108
        bank = 0
        csum = 23
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def bolted_btn_relay2_clicked(self):
        # Turn on relay 2 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 109
        bank = 0
        csum = 24
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def bolted_btn_relay3_clicked(self):
        # Turn on relay 3 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 110
        bank = 0
        csum = 23
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def bolted_btn_relay4_clicked(self):
        # Turn on relay 4 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 111
        bank = 0
        csum = 24
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def bolted_btn_relay5_clicked(self):
        # Turn on relay 5 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 112
        bank = 0
        csum = 25
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def bolted_btn_relay6_clicked(self):
        # Turn on relay 6 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 113
        bank = 0
        csum = 26
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def bolted_btn_relay7_clicked(self):
        # Turn on relay 7 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 114
        bank = 0
        csum = 27
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

    def bolted_btn_relay8_clicked(self):
        # Turn on relay 8 for all banks (all phases and resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 115
        bank = 0
        csum = 28
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)

        # Turn off all relays for bank 2 (resistor bank)
        api1 = 170
        api2 = 3
        api3 = 254
        ctrl = 129
        bank = 2
        csum = 46
        tx = [api1, api2, api3, ctrl, bank, csum]
        serial_transmit(tx)


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
