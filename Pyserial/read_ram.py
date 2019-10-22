def read_position(serial):
    data = 'FF FF 01 04 02 38 02 BE'
    data_send = bytes.fromhex(data)
    serial.write(data_send)
    data_read = serial.readline()
    read = data_read.hex()

    return read