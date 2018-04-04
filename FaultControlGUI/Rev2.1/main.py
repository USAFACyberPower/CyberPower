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
        self.ui = loadUi('FaultControlGUI_Rev2.1.ui', self)

    # ONE LINE MAIN MENU
        # Set the default menu page
        self.ui.stackedWidget.setCurrentIndex(0)

    # FAULT LOCATION 1
        # Fault Location 1 - Menu Functions
        self.btn_OneLine_loc1TL1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.btn_loc1_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc1_reset.clicked.connect(self.btn_reset_clicked)
        self.ui.stackedWidget_Loc1.setCurrentIndex(0)
        self.btn_loc1_select.clicked.connect(lambda: self.ui.stackedWidget_Loc1.setCurrentIndex(0))
        self.btn_loc1_selectA.clicked.connect(lambda: self.ui.stackedWidget_Loc1.setCurrentIndex(1))
        self.btn_loc1_selectB.clicked.connect(lambda: self.ui.stackedWidget_Loc1.setCurrentIndex(2))
        self.btn_loc1_selectC.clicked.connect(lambda: self.ui.stackedWidget_Loc1.setCurrentIndex(3))
        self.btn_loc1_selectM.clicked.connect(lambda: self.ui.stackedWidget_Loc1.setCurrentIndex(4))

        # Fault Location 1 - A Phase Faults
        self.btn_loc1_A200.clicked.connect(self.btn_loc1_A200_clicked)
        self.btn_loc1_A100.clicked.connect(self.btn_loc1_A100_clicked)
        self.btn_loc1_A67.clicked.connect(self.btn_loc1_A67_clicked)
        self.btn_loc1_A50.clicked.connect(self.btn_loc1_A50_clicked)
        self.btn_loc1_Abolt.clicked.connect(self.btn_loc1_Abolt_clicked)

        # Fault Location 1 - B Phase Faults
        self.btn_loc1_B200.clicked.connect(self.btn_loc1_B200_clicked)
        self.btn_loc1_B100.clicked.connect(self.btn_loc1_B100_clicked)
        self.btn_loc1_B67.clicked.connect(self.btn_loc1_B67_clicked)
        self.btn_loc1_B50.clicked.connect(self.btn_loc1_B50_clicked)
        self.btn_loc1_Bbolt.clicked.connect(self.btn_loc1_Bbolt_clicked)

        # Fault Location 1 - C Phase Faults
        self.btn_loc1_C200.clicked.connect(self.btn_loc1_C200_clicked)
        self.btn_loc1_C100.clicked.connect(self.btn_loc1_C100_clicked)
        self.btn_loc1_C67.clicked.connect(self.btn_loc1_C67_clicked)
        self.btn_loc1_C50.clicked.connect(self.btn_loc1_C50_clicked)
        self.btn_loc1_Cbolt.clicked.connect(self.btn_loc1_Cbolt_clicked)

        # Fault Location 1 - Multi-Phase Faults
        self.btn_loc1_AB.clicked.connect(self.btn_loc1_AB_clicked)
        self.btn_loc1_AC.clicked.connect(self.btn_loc1_AC_clicked)
        self.btn_loc1_BC.clicked.connect(self.btn_loc1_BC_clicked)
        self.btn_loc1_ABC.clicked.connect(self.btn_loc1_ABC_clicked)
        self.btn_loc1_GRND.clicked.connect(self.btn_GRND_clicked)

    # FAULT LOCATION 2
        # Fault Location 2 - Menu Functions
        self.btn_OneLine_loc2TL5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.btn_loc2_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc2_reset.clicked.connect(self.btn_reset_clicked)
        self.ui.stackedWidget_Loc2.setCurrentIndex(0)
        self.btn_loc2_select.clicked.connect(lambda: self.ui.stackedWidget_Loc2.setCurrentIndex(0))
        self.btn_loc2_selectA.clicked.connect(lambda: self.ui.stackedWidget_Loc2.setCurrentIndex(1))
        self.btn_loc2_selectB.clicked.connect(lambda: self.ui.stackedWidget_Loc2.setCurrentIndex(2))
        self.btn_loc2_selectC.clicked.connect(lambda: self.ui.stackedWidget_Loc2.setCurrentIndex(3))
        self.btn_loc2_selectM.clicked.connect(lambda: self.ui.stackedWidget_Loc2.setCurrentIndex(4))

        # Fault Location 2 - A Phase Faults
        self.btn_loc2_A200.clicked.connect(self.btn_loc2_A200_clicked)
        self.btn_loc2_A100.clicked.connect(self.btn_loc2_A100_clicked)
        self.btn_loc2_A67.clicked.connect(self.btn_loc2_A67_clicked)
        self.btn_loc2_A50.clicked.connect(self.btn_loc2_A50_clicked)
        self.btn_loc2_Abolt.clicked.connect(self.btn_loc2_Abolt_clicked)

        # Fault Location 2 - B Phase Faults
        self.btn_loc2_B200.clicked.connect(self.btn_loc2_B200_clicked)
        self.btn_loc2_B100.clicked.connect(self.btn_loc2_B100_clicked)
        self.btn_loc2_B67.clicked.connect(self.btn_loc2_B67_clicked)
        self.btn_loc2_B50.clicked.connect(self.btn_loc2_B50_clicked)
        self.btn_loc2_Bbolt.clicked.connect(self.btn_loc2_Bbolt_clicked)

        # Fault Location 2 - C Phase Faults
        self.btn_loc2_C200.clicked.connect(self.btn_loc2_C200_clicked)
        self.btn_loc2_C100.clicked.connect(self.btn_loc2_C100_clicked)
        self.btn_loc2_C67.clicked.connect(self.btn_loc2_C67_clicked)
        self.btn_loc2_C50.clicked.connect(self.btn_loc2_C50_clicked)
        self.btn_loc2_Cbolt.clicked.connect(self.btn_loc2_Cbolt_clicked)

        # Fault Location 2 - Multi-Phase Faults
        self.btn_loc2_AB.clicked.connect(self.btn_loc2_AB_clicked)
        self.btn_loc2_AC.clicked.connect(self.btn_loc2_AC_clicked)
        self.btn_loc2_BC.clicked.connect(self.btn_loc2_BC_clicked)
        self.btn_loc2_ABC.clicked.connect(self.btn_loc2_ABC_clicked)
        self.btn_loc2_GRND.clicked.connect(self.btn_GRND_clicked)

    # FAULT LOCATION 3
        # Fault Location 3 - Menu Functions
        self.btn_OneLine_loc3TL4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.btn_loc3_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc3_reset.clicked.connect(self.btn_reset_clicked)
        self.ui.stackedWidget_Loc3.setCurrentIndex(0)
        self.btn_loc3_select.clicked.connect(lambda: self.ui.stackedWidget_Loc3.setCurrentIndex(0))
        self.btn_loc3_selectA.clicked.connect(lambda: self.ui.stackedWidget_Loc3.setCurrentIndex(1))
        self.btn_loc3_selectB.clicked.connect(lambda: self.ui.stackedWidget_Loc3.setCurrentIndex(2))
        self.btn_loc3_selectC.clicked.connect(lambda: self.ui.stackedWidget_Loc3.setCurrentIndex(3))
        self.btn_loc3_selectM.clicked.connect(lambda: self.ui.stackedWidget_Loc3.setCurrentIndex(4))

        # Fault Location 3 - A Phase Faults
        self.btn_loc3_A200.clicked.connect(self.btn_loc3_A200_clicked)
        self.btn_loc3_A100.clicked.connect(self.btn_loc3_A100_clicked)
        self.btn_loc3_A67.clicked.connect(self.btn_loc3_A67_clicked)
        self.btn_loc3_A50.clicked.connect(self.btn_loc3_A50_clicked)
        self.btn_loc3_Abolt.clicked.connect(self.btn_loc3_Abolt_clicked)

        # Fault Location 3 - B Phase Faults
        self.btn_loc3_B200.clicked.connect(self.btn_loc3_B200_clicked)
        self.btn_loc3_B100.clicked.connect(self.btn_loc3_B100_clicked)
        self.btn_loc3_B67.clicked.connect(self.btn_loc3_B67_clicked)
        self.btn_loc3_B50.clicked.connect(self.btn_loc3_B50_clicked)
        self.btn_loc3_Bbolt.clicked.connect(self.btn_loc3_Bbolt_clicked)

        # Fault Location 3 - C Phase Faults
        self.btn_loc3_C200.clicked.connect(self.btn_loc3_C200_clicked)
        self.btn_loc3_C100.clicked.connect(self.btn_loc3_C100_clicked)
        self.btn_loc3_C67.clicked.connect(self.btn_loc3_C67_clicked)
        self.btn_loc3_C50.clicked.connect(self.btn_loc3_C50_clicked)
        self.btn_loc3_Cbolt.clicked.connect(self.btn_loc3_Cbolt_clicked)

        # Fault Location 3 - Multi-Phase Faults
        self.btn_loc3_AB.clicked.connect(self.btn_loc3_AB_clicked)
        self.btn_loc3_AC.clicked.connect(self.btn_loc3_AC_clicked)
        self.btn_loc3_BC.clicked.connect(self.btn_loc3_BC_clicked)
        self.btn_loc3_ABC.clicked.connect(self.btn_loc3_ABC_clicked)
        self.btn_loc3_GRND.clicked.connect(self.btn_GRND_clicked)

    # FAULT LOCATION 4
        # Fault Location 4 - Menu Functions
        self.btn_OneLine_loc4TL7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.btn_loc4_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc4_reset.clicked.connect(self.btn_reset_clicked)
        self.ui.stackedWidget_Loc4.setCurrentIndex(0)
        self.btn_loc4_select.clicked.connect(lambda: self.ui.stackedWidget_Loc4.setCurrentIndex(0))
        self.btn_loc4_selectA.clicked.connect(lambda: self.ui.stackedWidget_Loc4.setCurrentIndex(1))
        self.btn_loc4_selectB.clicked.connect(lambda: self.ui.stackedWidget_Loc4.setCurrentIndex(2))
        self.btn_loc4_selectC.clicked.connect(lambda: self.ui.stackedWidget_Loc4.setCurrentIndex(3))
        self.btn_loc4_selectM.clicked.connect(lambda: self.ui.stackedWidget_Loc4.setCurrentIndex(4))

        # Fault Location 4 - A Phase Faults
        self.btn_loc4_A200.clicked.connect(self.btn_loc4_A200_clicked)
        self.btn_loc4_A100.clicked.connect(self.btn_loc4_A100_clicked)
        self.btn_loc4_A67.clicked.connect(self.btn_loc4_A67_clicked)
        self.btn_loc4_A50.clicked.connect(self.btn_loc4_A50_clicked)
        self.btn_loc4_Abolt.clicked.connect(self.btn_loc4_Abolt_clicked)

        # Fault Location 4 - B Phase Faults
        self.btn_loc4_B200.clicked.connect(self.btn_loc4_B200_clicked)
        self.btn_loc4_B100.clicked.connect(self.btn_loc4_B100_clicked)
        self.btn_loc4_B67.clicked.connect(self.btn_loc4_B67_clicked)
        self.btn_loc4_B50.clicked.connect(self.btn_loc4_B50_clicked)
        self.btn_loc4_Bbolt.clicked.connect(self.btn_loc4_Bbolt_clicked)

        # Fault Location 4 - C Phase Faults
        self.btn_loc4_C200.clicked.connect(self.btn_loc4_C200_clicked)
        self.btn_loc4_C100.clicked.connect(self.btn_loc4_C100_clicked)
        self.btn_loc4_C67.clicked.connect(self.btn_loc4_C67_clicked)
        self.btn_loc4_C50.clicked.connect(self.btn_loc4_C50_clicked)
        self.btn_loc4_Cbolt.clicked.connect(self.btn_loc4_Cbolt_clicked)

        # Fault Location 4 - Multi-Phase Faults
        self.btn_loc4_AB.clicked.connect(self.btn_loc4_AB_clicked)
        self.btn_loc4_AC.clicked.connect(self.btn_loc4_AC_clicked)
        self.btn_loc4_BC.clicked.connect(self.btn_loc4_BC_clicked)
        self.btn_loc4_ABC.clicked.connect(self.btn_loc4_ABC_clicked)
        self.btn_loc4_GRND.clicked.connect(self.btn_GRND_clicked)

    # FAULT LOCATION 5
        # Fault Location 5 - Menu Functions
        self.btn_OneLine_loc5TL9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.btn_loc5_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc5_reset.clicked.connect(self.btn_reset_clicked)
        self.ui.stackedWidget_Loc5.setCurrentIndex(0)
        self.btn_loc5_select.clicked.connect(lambda: self.ui.stackedWidget_Loc5.setCurrentIndex(0))
        self.btn_loc5_selectA.clicked.connect(lambda: self.ui.stackedWidget_Loc5.setCurrentIndex(1))
        self.btn_loc5_selectB.clicked.connect(lambda: self.ui.stackedWidget_Loc5.setCurrentIndex(2))
        self.btn_loc5_selectC.clicked.connect(lambda: self.ui.stackedWidget_Loc5.setCurrentIndex(3))
        self.btn_loc5_selectM.clicked.connect(lambda: self.ui.stackedWidget_Loc5.setCurrentIndex(4))

        # Fault Location 5 - A Phase Faults
        self.btn_loc5_A200.clicked.connect(self.btn_loc5_A200_clicked)
        self.btn_loc5_A100.clicked.connect(self.btn_loc5_A100_clicked)
        self.btn_loc5_A67.clicked.connect(self.btn_loc5_A67_clicked)
        self.btn_loc5_A50.clicked.connect(self.btn_loc5_A50_clicked)
        self.btn_loc5_Abolt.clicked.connect(self.btn_loc5_Abolt_clicked)

        # Fault Location 5 - B Phase Faults
        self.btn_loc5_B200.clicked.connect(self.btn_loc5_B200_clicked)
        self.btn_loc5_B100.clicked.connect(self.btn_loc5_B100_clicked)
        self.btn_loc5_B67.clicked.connect(self.btn_loc5_B67_clicked)
        self.btn_loc5_B50.clicked.connect(self.btn_loc5_B50_clicked)
        self.btn_loc5_Bbolt.clicked.connect(self.btn_loc5_Bbolt_clicked)

        # Fault Location 5 - C Phase Faults
        self.btn_loc5_C200.clicked.connect(self.btn_loc5_C200_clicked)
        self.btn_loc5_C100.clicked.connect(self.btn_loc5_C100_clicked)
        self.btn_loc5_C67.clicked.connect(self.btn_loc5_C67_clicked)
        self.btn_loc5_C50.clicked.connect(self.btn_loc5_C50_clicked)
        self.btn_loc5_Cbolt.clicked.connect(self.btn_loc5_Cbolt_clicked)

        # Fault Location 5 - Multi-Phase Faults
        self.btn_loc5_AB.clicked.connect(self.btn_loc5_AB_clicked)
        self.btn_loc5_AC.clicked.connect(self.btn_loc5_AC_clicked)
        self.btn_loc5_BC.clicked.connect(self.btn_loc5_BC_clicked)
        self.btn_loc5_ABC.clicked.connect(self.btn_loc5_ABC_clicked)
        self.btn_loc5_GRND.clicked.connect(self.btn_GRND_clicked)

    # FAULT LOCATION 6
        # Fault Location 6 - Menu Functions
        self.btn_OneLine_loc6TL6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        self.btn_loc6_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loc6_reset.clicked.connect(self.btn_reset_clicked)
        self.ui.stackedWidget_Loc6.setCurrentIndex(0)
        self.btn_loc6_select.clicked.connect(lambda: self.ui.stackedWidget_Loc6.setCurrentIndex(0))
        self.btn_loc6_selectA.clicked.connect(lambda: self.ui.stackedWidget_Loc6.setCurrentIndex(1))
        self.btn_loc6_selectB.clicked.connect(lambda: self.ui.stackedWidget_Loc6.setCurrentIndex(2))
        self.btn_loc6_selectC.clicked.connect(lambda: self.ui.stackedWidget_Loc6.setCurrentIndex(3))
        self.btn_loc6_selectM.clicked.connect(lambda: self.ui.stackedWidget_Loc6.setCurrentIndex(4))

        # Fault Location 6 - A Phase Faults
        self.btn_loc6_A200.clicked.connect(self.btn_loc6_A200_clicked)
        self.btn_loc6_A100.clicked.connect(self.btn_loc6_A100_clicked)
        self.btn_loc6_A67.clicked.connect(self.btn_loc6_A67_clicked)
        self.btn_loc6_A50.clicked.connect(self.btn_loc6_A50_clicked)
        self.btn_loc6_Abolt.clicked.connect(self.btn_loc6_Abolt_clicked)

        # Fault Location 6 - B Phase Faults
        self.btn_loc6_B200.clicked.connect(self.btn_loc6_B200_clicked)
        self.btn_loc6_B100.clicked.connect(self.btn_loc6_B100_clicked)
        self.btn_loc6_B67.clicked.connect(self.btn_loc6_B67_clicked)
        self.btn_loc6_B50.clicked.connect(self.btn_loc6_B50_clicked)
        self.btn_loc6_Bbolt.clicked.connect(self.btn_loc6_Bbolt_clicked)

        # Fault Location 6 - C Phase Faults
        self.btn_loc6_C200.clicked.connect(self.btn_loc6_C200_clicked)
        self.btn_loc6_C100.clicked.connect(self.btn_loc6_C100_clicked)
        self.btn_loc6_C67.clicked.connect(self.btn_loc6_C67_clicked)
        self.btn_loc6_C50.clicked.connect(self.btn_loc6_C50_clicked)
        self.btn_loc6_Cbolt.clicked.connect(self.btn_loc6_Cbolt_clicked)

        # Fault Location 6 - Multi-Phase Faults
        self.btn_loc6_AB.clicked.connect(self.btn_loc6_AB_clicked)
        self.btn_loc6_AC.clicked.connect(self.btn_loc6_AC_clicked)
        self.btn_loc6_BC.clicked.connect(self.btn_loc6_BC_clicked)
        self.btn_loc6_ABC.clicked.connect(self.btn_loc6_ABC_clicked)
        self.btn_loc6_GRND.clicked.connect(self.btn_GRND_clicked)

    @pyqtSlot()
# BEGIN MAIN MENU DEFINITIONS
    # All Locations - Master Reset
    def btn_reset_clicked(self):
        # Reset All
        tx = [170, 3, 254, 129, 0, 44]
        serial_transmit(tx)

    def btn_GRND_clicked(self):
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
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

    def btn_loc1_Abolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 108, 1, 24]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
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

    def btn_loc1_Bbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 108, 3, 26]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
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

    def btn_loc1_Cbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 108, 4, 27]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
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

    def btn_loc1_ABC_clicked(self):
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

# BEGIN LOCATION 2 FAULT DEFINITIONS
    # Fault Location 2 - A Phase Resistive Faults
    def btn_loc2_A200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)

    def btn_loc2_A100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)

    def btn_loc2_A67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)

    def btn_loc2_A50_clicked(self):
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
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)

    def btn_loc2_Abolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 2 - B Phase Resistive Faults
    def btn_loc2_B200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)

    def btn_loc2_B100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)

    def btn_loc2_B67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)

    def btn_loc2_B50_clicked(self):
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
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)

    def btn_loc2_Bbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 2 - C Phase Resistive Faults
    def btn_loc2_C200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)

    def btn_loc2_C100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)

    def btn_loc2_C67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)

    def btn_loc2_C50_clicked(self):
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
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)

    def btn_loc2_Cbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 2 - Multi-Phase Faults
    def btn_loc2_AB_clicked(self):
        # Phase A
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)

    def btn_loc2_AC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)

    def btn_loc2_BC_clicked(self):
        # Phase B
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)

    def btn_loc2_ABC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 109, 1, 25]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 109, 3, 27]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 109, 4, 28]
        serial_transmit(tx)

# END LOCATION 2 FAULT DEFINITIONS

# BEGIN LOCATION 3 FAULT DEFINITIONS
    # Fault Location 3 - A Phase Resistive Faults
    def btn_loc3_A200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)

    def btn_loc3_A100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)

    def btn_loc3_A67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)

    def btn_loc3_A50_clicked(self):
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
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)

    def btn_loc3_Abolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 3 - B Phase Resistive Faults
    def btn_loc3_B200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)

    def btn_loc3_B100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)

    def btn_loc3_B67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)

    def btn_loc3_B50_clicked(self):
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
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)

    def btn_loc3_Bbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 3 - C Phase Resistive Faults
    def btn_loc3_C200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)

    def btn_loc3_C100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)

    def btn_loc3_C67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)

    def btn_loc3_C50_clicked(self):
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
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)

    def btn_loc3_Cbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 3 - Multi-Phase Faults
    def btn_loc3_AB_clicked(self):
        # Phase A
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)

    def btn_loc3_AC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)

    def btn_loc3_BC_clicked(self):
        # Phase B
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)

    def btn_loc3_ABC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 110, 1, 26]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 110, 3, 28]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 110, 4, 29]
        serial_transmit(tx)

# END LOCATION 3 FAULT DEFINITIONS

# BEGIN LOCATION 4 FAULT DEFINITIONS
    # Fault Location 4 - A Phase Resistive Faults
    def btn_loc4_A200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)

    def btn_loc4_A100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)

    def btn_loc4_A67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)

    def btn_loc4_A50_clicked(self):
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
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)

    def btn_loc4_Abolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 4 - B Phase Resistive Faults
    def btn_loc4_B200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)

    def btn_loc4_B100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)

    def btn_loc4_B67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)

    def btn_loc4_B50_clicked(self):
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
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)

    def btn_loc4_Bbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 4 - C Phase Resistive Faults
    def btn_loc4_C200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)

    def btn_loc4_C100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)

    def btn_loc4_C67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)

    def btn_loc4_C50_clicked(self):
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
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)

    def btn_loc4_Cbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 4 - Multi-Phase Faults
    def btn_loc4_AB_clicked(self):
        # Phase A
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)

    def btn_loc4_AC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)

    def btn_loc4_BC_clicked(self):
        # Phase B
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)

    def btn_loc4_ABC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 111, 1, 27]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 111, 3, 29]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 111, 4, 30]
        serial_transmit(tx)

# END LOCATION 4 FAULT DEFINITIONS

# BEGIN LOCATION 5 FAULT DEFINITIONS
    # Fault Location 5 - A Phase Resistive Faults
    def btn_loc5_A200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)

    def btn_loc5_A100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)

    def btn_loc5_A67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)

    def btn_loc5_A50_clicked(self):
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
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)

    def btn_loc5_Abolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 5 - B Phase Resistive Faults
    def btn_loc5_B200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)

    def btn_loc5_B100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)

    def btn_loc5_B67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)

    def btn_loc5_B50_clicked(self):
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
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)

    def btn_loc5_Bbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location5 - C Phase Resistive Faults
    def btn_loc5_C200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)

    def btn_loc5_C100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)

    def btn_loc5_C67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)

    def btn_loc5_C50_clicked(self):
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
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)

    def btn_loc5_Cbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location5 - Multi-Phase Faults
    def btn_loc5_AB_clicked(self):
        # Phase A
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)

    def btn_loc5_AC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)

    def btn_loc5_BC_clicked(self):
        # Phase B
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)

    def btn_loc5_ABC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 112, 1, 28]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 112, 3, 30]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 112, 4, 31]
        serial_transmit(tx)

# END LOCATION 5 FAULT DEFINITIONS

# BEGIN LOCATION 6 FAULT DEFINITIONS
    # Fault Location 6 - A Phase Resistive Faults
    def btn_loc6_A200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)

    def btn_loc6_A100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)

    def btn_loc6_A67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)

    def btn_loc6_A50_clicked(self):
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
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)

    def btn_loc6_Abolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location 6 - B Phase Resistive Faults
    def btn_loc6_B200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)

    def btn_loc6_B100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)

    def btn_loc6_B67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)

    def btn_loc6_B50_clicked(self):
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
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)

    def btn_loc6_Bbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location5 - C Phase Resistive Faults
    def btn_loc6_C200_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)

    def btn_loc6_C100_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)

    def btn_loc6_C67_clicked(self):
        # Prep Resistor Bank
        tx = [170, 3, 254, 108, 2, 25]
        serial_transmit(tx)
        tx = [170, 3, 254, 109, 2, 26]
        serial_transmit(tx)
        tx = [170, 3, 254, 110, 2, 27]
        serial_transmit(tx)
        # Close Phase Switch
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)

    def btn_loc6_C50_clicked(self):
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
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)

    def btn_loc6_Cbolt_clicked(self):
        # Relay Select
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)
        # Ground Enable
        tx = [170, 3, 254, 112, 2, 29]
        serial_transmit(tx)

    # Fault Location5 - Multi-Phase Faults
    def btn_loc6_AB_clicked(self):
        # Phase A
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)

    def btn_loc6_AC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)

    def btn_loc6_BC_clicked(self):
        # Phase B
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)

    def btn_loc6_ABC_clicked(self):
        # Phase A
        tx = [170, 3, 254, 113, 1, 29]
        serial_transmit(tx)
        # Phase B
        tx = [170, 3, 254, 113, 3, 31]
        serial_transmit(tx)
        # Phase C
        tx = [170, 3, 254, 113, 4, 32]
        serial_transmit(tx)

# END LOCATION 6 FAULT DEFINITIONS


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
