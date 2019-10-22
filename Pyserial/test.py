import serial
import time
import test_map

ser=serial.Serial("/dev/ttyUSB0",9600,timeout=0.5)
ser.baudrate=9600 #设置波特率
ser.bytesize=8 #字节大小
ser.parity=serial.PARITY_NONE #无校验
ser.stopbits=1 #停止位
ser.timeout=0.5 #读超时设置

stack= []
count = 0 
N = 100         #
T = 0.1
#ser.open() #打开端口
for i in range(N):
    s = ser.readline()#从端口读
    thickness = s.decode()
    thickness = thickness[:-2]
    if thickness == '---.--':
        stack.append(None)
        count +=1
    else:
        stack.append(float(thickness))
if count >= N //2:
    print('warnning: low valid points')
            
    time.sleep(T)
    
print(stack)
test_map.make_chart(stack)
ser.close()



#def make_chart (stack):
    