import sys
import serial

run = 1
while(run == 1):
    # Print the OPCODE description to the user.
    print("Enter Your Desired Opcode:\n")

    # Define the OPCODE here:
    api1 = 170
    api2 = 3
    api3 = 254
    ctrl = int(input("Enter the Control Command Byte: "))
    bank = int(input("Enter the Bank Command Byte: "))
    #csum = checksum function not known, only needed for opcode validation
    
    tx = [api1, api2, api3, ctrl, bank]

    # Establish USB Virtual Serial Connection
    ser = serial.Serial(
                         port='/dev/ttyUSB0',
                         baudrate=115200,
                         bytesize=serial.EIGHTBITS,
                         parity=serial.PARITY_NONE,
                         stopbits=serial.STOPBITS_ONE,
                         timeout=1
                         )
    
    # Print the OPCODE so the user can see what is being sent.
    print("Bytes Sent: "+str(tx))

    # Send OPCODE Serial Bits (TX) to Relay Board.
    ser.write(serial.to_bytes(tx))

    # Let the user know the command has completed.
    print("Done.")

    # Ask the user if they want to continue.
    run = int(input("Enter 1 to Continue: "))
