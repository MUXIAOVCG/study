import struct
'''
values = (1, 2, 3)
s = struct.Struct('I3sh')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)

print(values,packed_data,unpacked_data)
print(s)
'''
'''data = 867

data2 = struct.pack('i', 867)
data3 = struct.unpack('B',data2[0])

print(data2,data3)'''
'''d = 0x3 + 0x5
c = str(d)
a = '01 02 FF 01'
b = bytes.fromhex(a)
print(c,b)'''

'''position = 15
v = int(((position % 360) / 360)*4095)
V_hex = '{:0>4x}'.format(v)
V_send = V_hex[:2] + ' ' + V_hex[2:]

V_c = hex(~v)
t = hex(0xff + ~ (0x01 + 0x02 + 0x01) +1)
send = '01 02 1a 02'
x = send.split(' ')
print(V_hex,V_send,V_c,t)'''

'''
position = 359
id = 1
V_int = int(((position % 360) / 360)*4095)
Check_sum = 0x10000 + ~(id + 0x05 + 0x03 + 0x2A + V_int // 256 + V_int % 256)
a = id + 0x05 + 0x03 + 0x2A + V_int // 256 + V_int % 256

print(hex(Check_sum)[-2:], hex(a), hex(~a), hex(b))
'''
import serial #导入模块
'''
import serial.tools.list_ports
port_list = list(serial.tools.list_ports.comports())
print(port_list)
if len(port_list) == 0:
   print('无可用串口')
else:
    for i in range(0,len(port_list)):
        print(i,port_list[i])'''
'''id = 1
position = 100
id_send = '{:0>2d}'.format(id)
P_int = int(((position % 360) / 360) * 4095)
P_hex = '{:0>4x}'.format(P_int)
P_send = P_hex[:2] + ' ' + P_hex[2:]
Check_sum = 0x1000 + ~(id + 0x05 + 0x03 + 0x2A + P_int // 256 + P_int % 256)
data = 'FF FF ' + id_send + ' 05 03 2A ' + P_send + ' ' + hex(Check_sum)[-2:]
print(data)'''
print(0x205)