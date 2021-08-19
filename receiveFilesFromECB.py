import serial
import sys
from datetime import datetime, date

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

for l in ourSerial:
    if l.rstrip() == 'S0030000FC': #S0 record identifies beginning of transmission
        now = datetime.now()
        today = date.today()
        filename = today.strftime("%d%m%Y") + "_" + now.strftime("%H-%M-%S") + '.s'
        f = open (filename, 'w')
        count = 1
        sys.stdout.write('Writing from Motorola ECB to file "' + filename + '"... ')
        sys.stdout.flush()
    f.write(l.rstrip() + '\r\n') # S-format expects a carriage return
    count += 1
    if l.rstrip() == 'S9030000FC': #S9 record identifies end of transmission
        f.flush()
        f.close()
        sys.stdout.write('done. ' + str(count + 1) + ' lines written.\n')
        sys.stdout.flush()
