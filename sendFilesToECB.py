import serial
import sys

ourSerial = serial.Serial()
ourSerial.port = '/dev/ttySC1'
ourSerial.baudrate = 4800
ourSerial.bytesize = serial.EIGHTBITS
ourSerial.parity = serial.PARITY_NONE
ourSerial.stopbits = serial.STOPBITS_ONE
ourSerial.xonxoff = False
ourSerial.rtscts = False
ourSerial.dsrdtr = False

ourSerial.open()
ourSerial.flushInput()
ourSerial.flushOutput()

with open (sys.argv[1]) as fil:
    count = 1
    for li in fil:
        ourSerial.write(li)
        ourSerial.flush()
        count += 1

fil.close()
print str(count) + " lines written to Motorola ECB."

