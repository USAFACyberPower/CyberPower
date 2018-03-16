import sys
import serial
import resource
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

        # One Line Main Menu Functions
        self.ui.stackedWidget.setCurrentIndex(0)
        self.btn_OneLine_loc1TL1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.btn_OneLine_loc2TL5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.btn_OneLine_loc3TL4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.btn_OneLine_loc4TL7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.btn_OneLine_loc5TL9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.btn_OneLine_loc6TL6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))

        # Fault Location 1 - Menu Functions
        self.btn_OneLine_loc1TL1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.btn_loc1_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc1_reset.clicked.connect(self.btn_reset_clicked)
        # Fault Location 1 - A Phase Resistive Faults
        self.btn_loc1_A200.clicked.connect(self.btn_loc1_A200_clicked)
        self.btn_loc1_A100.clicked.connect(self.btn_loc1_A100_clicked)
        self.btn_loc1_A67.clicked.connect(self.btn_loc1_A67_clicked)
        self.btn_loc1_A50.clicked.connect(self.btn_loc1_A50_clicked)
        # Fault Location 1 - B Phase Resistive Faults
        self.btn_loc1_B200.clicked.connect(self.btn_loc1_B200_clicked)
        self.btn_loc1_B100.clicked.connect(self.btn_loc1_B100_clicked)
        self.btn_loc1_B67.clicked.connect(self.btn_loc1_B67_clicked)
        self.btn_loc1_B50.clicked.connect(self.btn_loc1_B50_clicked)
        # Fault Location 1 - C Phase Resistive Faults
        self.btn_loc1_C200.clicked.connect(self.btn_loc1_C200_clicked)
        self.btn_loc1_C100.clicked.connect(self.btn_loc1_C100_clicked)
        self.btn_loc1_C67.clicked.connect(self.btn_loc1_C67_clicked)
        self.btn_loc1_C50.clicked.connect(self.btn_loc1_C50_clicked)
        # Fault Location 1 - Multi-Phase Faults
        self.btn_loc1_AB.clicked.connect(self.btn_loc1_AB_clicked)
        self.btn_loc1_AC.clicked.connect(self.btn_loc1_AC_clicked)
        self.btn_loc1_BC.clicked.connect(self.btn_loc1_BC_clicked)
        self.btn_loc1_bolt.clicked.connect(self.btn_loc1_bolt_clicked)

        # Fault Location 2 - Menu Functions
        self.btn_OneLine_loc2TL5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.btn_loc2_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc2_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 3 - Menu Functions
        self.btn_OneLine_loc3TL4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.btn_loc3_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc3_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 4 - Menu Functions
        self.btn_OneLine_loc4TL7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.btn_loc4_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc4_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 5 - Menu Functions
        self.btn_OneLine_loc5TL9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.btn_loc5_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc5_reset.clicked.connect(self.btn_reset_clicked)

        # Fault Location 6 - Menu Functions
        self.btn_OneLine_loc6TL6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        self.btn_loc6_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc6_reset.clicked.connect(self.btn_reset_clicked)

    @pyqtSlot()
# BEGIN MAIN MENU DEFINITIONS
    # All Locations - Master Reset
    def btn_reset_clicked(self):
        # Reset All
        tx = [170, 3, 254, 129, 0, 44]
        serial_transmit(tx)
# END MAIN MENU DEFINITIONS

# BEGIN LOCATION 1 FAULT DEFINITIONS
    # Fault Location 1 - A Phase Resistive Faults
    def btn_loc1_A200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)

    def btn_loc1_A100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)

    def btn_loc1_A67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)

    def btn_loc1_A50_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        tx = [170, 3, 254, 111, 2, 28]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)

    # Fault Location 1 - B Phase Resistive Faults
    def btn_loc1_B200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)

    def btn_loc1_B100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)

    def btn_loc1_B67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)

    def btn_loc1_B50_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        tx = [170, 3, 254, 111, 2, 28]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)

    # Fault Location 1 - C Phase Resistive Faults
    def btn_loc1_C200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)

    def btn_loc1_C100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)

    def btn_loc1_C67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)

    def btn_loc1_C50_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        tx = [170, 3, 254, 111, 2, 28]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)

    # Fault Location 1 - Multi-Phase Faults
    def btn_loc1_AB_clicked(self):
        # Phase A
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)

    def btn_loc1_AC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)

    def btn_loc1_BC_clicked(self):
        # Phase B
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)

    def btn_loc1_bolt_clicked(self):
        # Phase A
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)
# END LOCATION 1 FAULT DEFINITIONS


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
