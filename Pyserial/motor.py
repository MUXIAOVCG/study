import serial
import time
import test_map
import data_send

#ser=serial.Serial("/dev/ttyUSB0",115200,timeout=0.5)
ser=serial.Serial("COM4",115200,timeout=0.5)

ser.baudrate=115200 #设置波特率
ser.bytesize=8 #字节大小
ser.parity=serial.PARITY_NONE #无校验
ser.stopbits=1 #停止位
ser.timeout=0.5 #读超时设置

position = 90
print(data_send.check_status(1, ser))
print(data_send.move(1, ser, position))
# time.sleep(3)
cur = 0
while abs(cur - position) > 0.3:
    cur = float(data_send.read_position(1, ser))
    print(cur)
    time.sleep(0.05)
print(1)

'''id = 1
for i in range(10):
    position = i * 5 + 0.25
    print(data_send.check_status(1,ser))
    print(data_send.move(1,ser,position))
    #time.sleep(3)
    cur = 0
    while abs(cur - position) > 0.25:
        cur = float(data_send.read_position(1, ser))
        print(cur)
        time.sleep(0.05)
    print(1)
'''

