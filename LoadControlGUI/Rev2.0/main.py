import sys
import serial
import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLineEdit, QLCDNumber
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
        self.ui.stackedWidget.setCurrentIndex(0)
        self.btn_Unbalanced.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.btn_Balanced.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.btn_loadResetB.clicked.connect(self.btn_reset_clicked)
        self.btn_loadResetU.clicked.connect(self.btn_reset_clicked)

    # BALANCED LOAD SLIDER
        # LED Indicator Setup for Watt and Ohm Displays
        self.lcdNumber_Watts.display(self.balancedLoadValueChange())
        self.lcdNumber_Ohms.display(self.balancedLoadValueChange())
        # Load Slider Setup for Watt and Ohm Displays
        self.horizontalSlider_loadSelecter.valueChanged.connect(self.balancedLoadValueChange)

    # UNBALANCED LOAD SLIDERS
        # LED Indicator Setup for Watt and Ohm Displays
        self.lcdNumber_WattsA.display(self.unbalancedLoadValueChangeA())
        self.lcdNumber_OhmsA.display(self.unbalancedLoadValueChangeA())
        self.lcdNumber_WattsB.display(self.unbalancedLoadValueChangeB())
        self.lcdNumber_OhmsB.display(self.unbalancedLoadValueChangeB())
        self.lcdNumber_WattsC.display(self.unbalancedLoadValueChangeC())
        self.lcdNumber_OhmsC.display(self.unbalancedLoadValueChangeC())
        # Load Slider Setup for Watt and Ohm Displays
        self.verticalSlider_LoadA.valueChanged.connect(self.unbalancedLoadValueChangeA)
        self.verticalSlider_LoadB.valueChanged.connect(self.unbalancedLoadValueChangeB)
        self.verticalSlider_LoadC.valueChanged.connect(self.unbalancedLoadValueChangeC)


    @pyqtSlot()
# BEGIN MAIN MENU DEFINITIONS
    # Master Reset
    def btn_reset_clicked(self):
        # Reset All
        tx = [170, 3, 254, 129, 0, 44]
        serial_transmit(tx)
# END MAIN MENU DEFINITIONS

# BEGIN BALANCED SLIDER/LED FUNCTIONS
    def balancedLoadValueChange(self):
        # Updates the LCD displays for balanced slider values
        balancedSlider = str(self.horizontalSlider_loadSelecter.value())
        if balancedSlider == '0':
            self.lcdNumber_Watts.display(0)
            self.lcdNumber_Ohms.display(0)
        elif balancedSlider == '1':
            self.lcdNumber_Watts.display(0.77)
            self.lcdNumber_Ohms.display(750)
        elif balancedSlider == '2':
            self.lcdNumber_Watts.display(1.0)
            self.lcdNumber_Ohms.display(600)
        elif balancedSlider == '3':
            self.lcdNumber_Watts.display(1.4)
            self.lcdNumber_Ohms.display(400)
        elif balancedSlider == '4':
            self.lcdNumber_Watts.display(1.7)
            self.lcdNumber_Ohms.display(333.3)
        elif balancedSlider == '5':
            self.lcdNumber_Watts.display(2.2)
            self.lcdNumber_Ohms.display(260.9)
        elif balancedSlider == '6':
            self.lcdNumber_Watts.display(2.4)
            self.lcdNumber_Ohms.display(240)
        elif balancedSlider == '7':
            self.lcdNumber_Watts.display(2.9)
            self.lcdNumber_Ohms.display(200)
        elif balancedSlider == '8':
            self.lcdNumber_Watts.display(3.2)
            self.lcdNumber_Ohms.display(181.8)
        elif balancedSlider == '9':
            self.lcdNumber_Watts.display(3.6)
            self.lcdNumber_Ohms.display(157.9)
        elif balancedSlider == '10':
            self.lcdNumber_Watts.display(3.8)
            self.lcdNumber_Ohms.display(150)
        elif balancedSlider == '11':
            self.lcdNumber_Watts.display(4.3)
            self.lcdNumber_Ohms.display(133.3)
        elif balancedSlider == '12':
            self.lcdNumber_Watts.display(4.6)
            self.lcdNumber_Ohms.display(125)
        elif balancedSlider == '13':
            self.lcdNumber_Watts.display(5.1)
            self.lcdNumber_Ohms.display(113.2)
        elif balancedSlider == '14':
            self.lcdNumber_Watts.display(5.3)
            self.lcdNumber_Ohms.display(109.1)
        elif balancedSlider == '15':
            self.lcdNumber_Watts.display(5.8)
            self.lcdNumber_Ohms.display(100)
        elif balancedSlider == '16':
            self.lcdNumber_Watts.display(6.1)
            self.lcdNumber_Ohms.display(95.2)
        elif balancedSlider == '17':
            self.lcdNumber_Watts.display(6.5)
            self.lcdNumber_Ohms.display(88.2)
        elif balancedSlider == '18':
            self.lcdNumber_Watts.display(6.7)
            self.lcdNumber_Ohms.display(85.7)
        elif balancedSlider == '19':
            self.lcdNumber_Watts.display(7.2)
            self.lcdNumber_Ohms.display(80)
        elif balancedSlider == '20':
            self.lcdNumber_Watts.display(7.5)
            self.lcdNumber_Ohms.display(76.9)
        elif balancedSlider == '21':
            self.lcdNumber_Watts.display(8)
            self.lcdNumber_Ohms.display(72.3)
        elif balancedSlider == '22':
            self.lcdNumber_Watts.display(8.2)
            self.lcdNumber_Ohms.display(70.6)
        elif balancedSlider == '23':
            self.lcdNumber_Watts.display(8.6)
            self.lcdNumber_Ohms.display(66.7)
        elif balancedSlider == '24':
            self.lcdNumber_Watts.display(8.9)
            self.lcdNumber_Ohms.display(64.5)
        elif balancedSlider == '25':
            self.lcdNumber_Watts.display(9.4)
            self.lcdNumber_Ohms.display(61.2)
        elif balancedSlider == '26':
            self.lcdNumber_Watts.display(9.6)
            self.lcdNumber_Ohms.display(60)
        elif balancedSlider == '27':
            self.lcdNumber_Watts.display(10.1)
            self.lcdNumber_Ohms.display(57.1)
        elif balancedSlider == '28':
            self.lcdNumber_Watts.display(10.4)
            self.lcdNumber_Ohms.display(55.6)
        elif balancedSlider == '29':
            self.lcdNumber_Watts.display(10.8)
            self.lcdNumber_Ohms.display(53.1)
        elif balancedSlider == '30':
            self.lcdNumber_Watts.display(11)
            self.lcdNumber_Ohms.display(52.2)
        elif balancedSlider == '31':
            self.lcdNumber_Watts.display(11.8)
            self.lcdNumber_Ohms.display(48.8)
        else:
            self.lcdNumber_Watts.display('ERR')
            self.lcdNumber_Ohms.display('ERR')
# END BALANCED SLIDER/LED FUNCTIONS

# BEGIN UNBALANCED SLIDER/LED FUNCTIONS
    # Phase A Slider/LED Functions
    def unbalancedLoadValueChangeA(self):
        # Updates the LCD displays for Phase A slider values
        unbalancedSliderA = str(self.verticalSlider_LoadA.value())
        if unbalancedSliderA == '0':
            self.lcdNumber_WattsA.display(0)
            self.lcdNumber_OhmsA.display(0)
        elif unbalancedSliderA == '1':
            self.lcdNumber_WattsA.display(0.77)
            self.lcdNumber_OhmsA.display(750)
        elif unbalancedSliderA == '2':
            self.lcdNumber_WattsA.display(1.0)
            self.lcdNumber_OhmsA.display(600)
        elif unbalancedSliderA == '3':
            self.lcdNumber_WattsA.display(1.4)
            self.lcdNumber_OhmsA.display(400)
        elif unbalancedSliderA == '4':
            self.lcdNumber_WattsA.display(1.7)
            self.lcdNumber_OhmsA.display(333.3)
        elif unbalancedSliderA == '5':
            self.lcdNumber_WattsA.display(2.2)
            self.lcdNumber_OhmsA.display(260.9)
        elif unbalancedSliderA == '6':
            self.lcdNumber_WattsA.display(2.4)
            self.lcdNumber_OhmsA.display(240)
        elif unbalancedSliderA == '7':
            self.lcdNumber_WattsA.display(2.9)
            self.lcdNumber_OhmsA.display(200)
        elif unbalancedSliderA == '8':
            self.lcdNumber_WattsA.display(3.2)
            self.lcdNumber_OhmsA.display(181.8)
        elif unbalancedSliderA == '9':
            self.lcdNumber_WattsA.display(3.6)
            self.lcdNumber_OhmsA.display(157.9)
        elif unbalancedSliderA == '10':
            self.lcdNumber_WattsA.display(3.8)
            self.lcdNumber_OhmsA.display(150)
        elif unbalancedSliderA == '11':
            self.lcdNumber_WattsA.display(4.3)
            self.lcdNumber_OhmsA.display(133.3)
        elif unbalancedSliderA == '12':
            self.lcdNumber_WattsA.display(4.6)
            self.lcdNumber_OhmsA.display(125)
        elif unbalancedSliderA == '13':
            self.lcdNumber_WattsA.display(5.1)
            self.lcdNumber_OhmsA.display(113.2)
        elif unbalancedSliderA == '14':
            self.lcdNumber_WattsA.display(5.3)
            self.lcdNumber_OhmsA.display(109.1)
        elif unbalancedSliderA == '15':
            self.lcdNumber_WattsA.display(5.8)
            self.lcdNumber_OhmsA.display(100)
        elif unbalancedSliderA == '16':
            self.lcdNumber_WattsA.display(6.1)
            self.lcdNumber_OhmsA.display(95.2)
        elif unbalancedSliderA == '17':
            self.lcdNumber_WattsA.display(6.5)
            self.lcdNumber_OhmsA.display(88.2)
        elif unbalancedSliderA == '18':
            self.lcdNumber_WattsA.display(6.7)
            self.lcdNumber_OhmsA.display(85.7)
        elif unbalancedSliderA == '19':
            self.lcdNumber_WattsA.display(7.2)
            self.lcdNumber_OhmsA.display(80)
        elif unbalancedSliderA == '20':
            self.lcdNumber_WattsA.display(7.5)
            self.lcdNumber_OhmsA.display(76.9)
        elif unbalancedSliderA == '21':
            self.lcdNumber_WattsA.display(8)
            self.lcdNumber_OhmsA.display(72.3)
        elif unbalancedSliderA == '22':
            self.lcdNumber_WattsA.display(8.2)
            self.lcdNumber_OhmsA.display(70.6)
        elif unbalancedSliderA == '23':
            self.lcdNumber_WattsA.display(8.6)
            self.lcdNumber_OhmsA.display(66.7)
        elif unbalancedSliderA == '24':
            self.lcdNumber_WattsA.display(8.9)
            self.lcdNumber_OhmsA.display(64.5)
        elif unbalancedSliderA == '25':
            self.lcdNumber_WattsA.display(9.4)
            self.lcdNumber_OhmsA.display(61.2)
        elif unbalancedSliderA == '26':
            self.lcdNumber_WattsA.display(9.6)
            self.lcdNumber_OhmsA.display(60)
        elif unbalancedSliderA == '27':
            self.lcdNumber_WattsA.display(10.1)
            self.lcdNumber_OhmsA.display(57.1)
        elif unbalancedSliderA == '28':
            self.lcdNumber_WattsA.display(10.4)
            self.lcdNumber_OhmsA.display(55.6)
        elif unbalancedSliderA == '29':
            self.lcdNumber_WattsA.display(10.8)
            self.lcdNumber_OhmsA.display(53.1)
        elif unbalancedSliderA == '30':
            self.lcdNumber_WattsA.display(11)
            self.lcdNumber_OhmsA.display(52.2)
        elif unbalancedSliderA == '31':
            self.lcdNumber_WattsA.display(11.8)
            self.lcdNumber_OhmsA.display(48.8)
        else:
            self.lcdNumber_WattsA.display('ERR')
            self.lcdNumber_OhmsA.display('ERR')

    # Phase B Slider/LED Functions
    def unbalancedLoadValueChangeB(self):
        # Updates the LCD displays for Phase B slider values
        unbalancedSliderB = str(self.verticalSlider_LoadB.value())
        if unbalancedSliderB == '0':
            self.lcdNumber_WattsB.display(0)
            self.lcdNumber_OhmsB.display(0)
        elif unbalancedSliderB == '1':
            self.lcdNumber_WattsB.display(0.77)
            self.lcdNumber_OhmsB.display(750)
        elif unbalancedSliderB == '2':
            self.lcdNumber_WattsB.display(1.0)
            self.lcdNumber_OhmsB.display(600)
        elif unbalancedSliderB == '3':
            self.lcdNumber_WattsB.display(1.4)
            self.lcdNumber_OhmsB.display(400)
        elif unbalancedSliderB == '4':
            self.lcdNumber_WattsB.display(1.7)
            self.lcdNumber_OhmsB.display(333.3)
        elif unbalancedSliderB == '5':
            self.lcdNumber_WattsB.display(2.2)
            self.lcdNumber_OhmsB.display(260.9)
        elif unbalancedSliderB == '6':
            self.lcdNumber_WattsB.display(2.4)
            self.lcdNumber_OhmsB.display(240)
        elif unbalancedSliderB == '7':
            self.lcdNumber_WattsB.display(2.9)
            self.lcdNumber_OhmsB.display(200)
        elif unbalancedSliderB == '8':
            self.lcdNumber_WattsB.display(3.2)
            self.lcdNumber_OhmsB.display(181.8)
        elif unbalancedSliderB == '9':
            self.lcdNumber_WattsB.display(3.6)
            self.lcdNumber_OhmsB.display(157.9)
        elif unbalancedSliderB == '10':
            self.lcdNumber_WattsB.display(3.8)
            self.lcdNumber_OhmsB.display(150)
        elif unbalancedSliderB == '11':
            self.lcdNumber_WattsB.display(4.3)
            self.lcdNumber_OhmsB.display(133.3)
        elif unbalancedSliderB == '12':
            self.lcdNumber_WattsB.display(4.6)
            self.lcdNumber_OhmsB.display(125)
        elif unbalancedSliderB == '13':
            self.lcdNumber_WattsB.display(5.1)
            self.lcdNumber_OhmsB.display(113.2)
        elif unbalancedSliderB == '14':
            self.lcdNumber_WattsB.display(5.3)
            self.lcdNumber_OhmsB.display(109.1)
        elif unbalancedSliderB == '15':
            self.lcdNumber_WattsB.display(5.8)
            self.lcdNumber_OhmsB.display(100)
        elif unbalancedSliderB == '16':
            self.lcdNumber_WattsB.display(6.1)
            self.lcdNumber_OhmsB.display(95.2)
        elif unbalancedSliderB == '17':
            self.lcdNumber_WattsB.display(6.5)
            self.lcdNumber_OhmsB.display(88.2)
        elif unbalancedSliderB == '18':
            self.lcdNumber_WattsB.display(6.7)
            self.lcdNumber_OhmsB.display(85.7)
        elif unbalancedSliderB == '19':
            self.lcdNumber_WattsB.display(7.2)
            self.lcdNumber_OhmsB.display(80)
        elif unbalancedSliderB == '20':
            self.lcdNumber_WattsB.display(7.5)
            self.lcdNumber_OhmsB.display(76.9)
        elif unbalancedSliderB == '21':
            self.lcdNumber_WattsB.display(8)
            self.lcdNumber_OhmsB.display(72.3)
        elif unbalancedSliderB == '22':
            self.lcdNumber_WattsB.display(8.2)
            self.lcdNumber_OhmsB.display(70.6)
        elif unbalancedSliderB == '23':
            self.lcdNumber_WattsB.display(8.6)
            self.lcdNumber_OhmsB.display(66.7)
        elif unbalancedSliderB == '24':
            self.lcdNumber_WattsB.display(8.9)
            self.lcdNumber_OhmsB.display(64.5)
        elif unbalancedSliderB == '25':
            self.lcdNumber_WattsB.display(9.4)
            self.lcdNumber_OhmsB.display(61.2)
        elif unbalancedSliderB == '26':
            self.lcdNumber_WattsB.display(9.6)
            self.lcdNumber_OhmsB.display(60)
        elif unbalancedSliderB == '27':
            self.lcdNumber_WattsB.display(10.1)
            self.lcdNumber_OhmsB.display(57.1)
        elif unbalancedSliderB == '28':
            self.lcdNumber_WattsB.display(10.4)
            self.lcdNumber_OhmsB.display(55.6)
        elif unbalancedSliderB == '29':
            self.lcdNumber_WattsB.display(10.8)
            self.lcdNumber_OhmsB.display(53.1)
        elif unbalancedSliderB == '30':
            self.lcdNumber_WattsB.display(11)
            self.lcdNumber_OhmsB.display(52.2)
        elif unbalancedSliderB == '31':
            self.lcdNumber_WattsB.display(11.8)
            self.lcdNumber_OhmsB.display(48.8)
        else:
            self.lcdNumber_WattsB.display('ERR')
            self.lcdNumber_OhmsB.display('ERR')

    # Phase C Slider/LED Functions
    def unbalancedLoadValueChangeC(self):
        # Updates the LCD displays for Phase C slider values
        unbalancedSliderC = str(self.verticalSlider_LoadC.value())
        if unbalancedSliderC == '0':
            self.lcdNumber_WattsC.display(0)
            self.lcdNumber_OhmsC.display(0)
        elif unbalancedSliderC == '1':
            self.lcdNumber_WattsC.display(0.77)
            self.lcdNumber_OhmsC.display(750)
        elif unbalancedSliderC == '2':
            self.lcdNumber_WattsC.display(1.0)
            self.lcdNumber_OhmsC.display(600)
        elif unbalancedSliderC == '3':
            self.lcdNumber_WattsC.display(1.4)
            self.lcdNumber_OhmsC.display(400)
        elif unbalancedSliderC == '4':
            self.lcdNumber_WattsC.display(1.7)
            self.lcdNumber_OhmsC.display(333.3)
        elif unbalancedSliderC == '5':
            self.lcdNumber_WattsC.display(2.2)
            self.lcdNumber_OhmsC.display(260.9)
        elif unbalancedSliderC == '6':
            self.lcdNumber_WattsC.display(2.4)
            self.lcdNumber_OhmsC.display(240)
        elif unbalancedSliderC == '7':
            self.lcdNumber_WattsC.display(2.9)
            self.lcdNumber_OhmsC.display(200)
        elif unbalancedSliderC == '8':
            self.lcdNumber_WattsC.display(3.2)
            self.lcdNumber_OhmsC.display(181.8)
        elif unbalancedSliderC == '9':
            self.lcdNumber_WattsC.display(3.6)
            self.lcdNumber_OhmsC.display(157.9)
        elif unbalancedSliderC == '10':
            self.lcdNumber_WattsC.display(3.8)
            self.lcdNumber_OhmsC.display(150)
        elif unbalancedSliderC == '11':
            self.lcdNumber_WattsC.display(4.3)
            self.lcdNumber_OhmsC.display(133.3)
        elif unbalancedSliderC == '12':
            self.lcdNumber_WattsC.display(4.6)
            self.lcdNumber_OhmsC.display(125)
        elif unbalancedSliderC == '13':
            self.lcdNumber_WattsC.display(5.1)
            self.lcdNumber_OhmsC.display(113.2)
        elif unbalancedSliderC == '14':
            self.lcdNumber_WattsC.display(5.3)
            self.lcdNumber_OhmsC.display(109.1)
        elif unbalancedSliderC == '15':
            self.lcdNumber_WattsC.display(5.8)
            self.lcdNumber_OhmsC.display(100)
        elif unbalancedSliderC == '16':
            self.lcdNumber_WattsC.display(6.1)
            self.lcdNumber_OhmsC.display(95.2)
        elif unbalancedSliderC == '17':
            self.lcdNumber_WattsC.display(6.5)
            self.lcdNumber_OhmsC.display(88.2)
        elif unbalancedSliderC == '18':
            self.lcdNumber_WattsC.display(6.7)
            self.lcdNumber_OhmsC.display(85.7)
        elif unbalancedSliderC == '19':
            self.lcdNumber_WattsC.display(7.2)
            self.lcdNumber_OhmsC.display(80)
        elif unbalancedSliderC == '20':
            self.lcdNumber_WattsC.display(7.5)
            self.lcdNumber_OhmsC.display(76.9)
        elif unbalancedSliderC == '21':
            self.lcdNumber_WattsC.display(8)
            self.lcdNumber_OhmsC.display(72.3)
        elif unbalancedSliderC == '22':
            self.lcdNumber_WattsC.display(8.2)
            self.lcdNumber_OhmsC.display(70.6)
        elif unbalancedSliderC == '23':
            self.lcdNumber_WattsC.display(8.6)
            self.lcdNumber_OhmsC.display(66.7)
        elif unbalancedSliderC == '24':
            self.lcdNumber_WattsC.display(8.9)
            self.lcdNumber_OhmsC.display(64.5)
        elif unbalancedSliderC == '25':
            self.lcdNumber_WattsC.display(9.4)
            self.lcdNumber_OhmsC.display(61.2)
        elif unbalancedSliderC == '26':
            self.lcdNumber_WattsC.display(9.6)
            self.lcdNumber_OhmsC.display(60)
        elif unbalancedSliderC == '27':
            self.lcdNumber_WattsC.display(10.1)
            self.lcdNumber_OhmsC.display(57.1)
        elif unbalancedSliderC == '28':
            self.lcdNumber_WattsC.display(10.4)
            self.lcdNumber_OhmsC.display(55.6)
        elif unbalancedSliderC == '29':
            self.lcdNumber_WattsC.display(10.8)
            self.lcdNumber_OhmsC.display(53.1)
        elif unbalancedSliderC == '30':
            self.lcdNumber_WattsC.display(11)
            self.lcdNumber_OhmsC.display(52.2)
        elif unbalancedSliderC == '31':
            self.lcdNumber_WattsC.display(11.8)
            self.lcdNumber_OhmsC.display(48.8)
        else:
            self.lcdNumber_WattsC.display('ERR')
            self.lcdNumber_OhmsC.display('ERR')
# END UNBALANCED SLIDER/LED FUNCTIONS


app = QApplication(sys.argv)
widget = App()
widget.show()
sys.exit(app.exec_())
