def check_status(id, serial):
    id_send = '{:0>2d}'.format(id)
    data = 'FF FF ' + id_send + ' 02 01 FB'
    data_send = bytes.fromhex(data)
    serial.write(data_send)
    #print(data_send)
    data_read = serial.readline()
    read = data_read.hex()
    return read


def move(id, serial, position):
    id_send = '{:0>2d}'.format(id)
    P_int = int(((position % 360) / 360) * 4095)
    P_hex = '{:0>4x}'.format(P_int)
    V_hex = ' 00 00 E8 03 '
    Check_sum = 0x1000 + ~(id + 0x09 + 0x03 + 0x2A + P_int // 256 + P_int % 256 + 0xE8 + 0x03)
    P_send = P_hex[2:] + ' ' + P_hex[:2]
    data = 'FF FF ' + id_send + ' 09 03 2A ' + P_send + V_hex + hex(Check_sum)[-2:]
    #print(P_send)
    data_send = bytes.fromhex(data)
    #print(data_send)
    serial.write(data_send)
    data_read = serial.readline()
    read = data_read.hex()
    return read


def read_position(id,serial):
    id_send = '{:0>2d}'.format(id)
    data = 'FF FF ' + id_send + ' 04 02 38 02 BE'
    data_send = bytes.fromhex(data)
    serial.write(data_send)
    data_read = serial.readline()
    read = data_read.hex()
    position = int('0x'+read[-4:-2] + read[-6:-4], 16)
    return format(position / 4095 * 360, '.4f')

