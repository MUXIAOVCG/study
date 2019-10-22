import serial


ser=serial.Serial("/dev/ttyUSB0",9600,timeout=0.5)
ser.baudrate=9600 #设置波特率
ser.bytesize=8 #字节大小
ser.parity=serial.PARITY_NONE #无校验
ser.stopbits=1 #停止位
ser.timeout=0.5 #读超时设置

#ser.open() #打开端口
for i in range(20):
    s = ser.readline()#从端口读10个字节
    thickness = s.decode()
    print(thickness)