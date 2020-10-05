import serial


port = "COM6"
conn = serial.Serial(port, 115200)


message = input("message: ")
conn.write(message.encode())
