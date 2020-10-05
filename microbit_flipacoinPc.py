import requests
import serial

port = "COM4"
conn = serial.Serial(port, 115200)

while True:
    input("Press Enter to flip a coin")
    r = requests.get("http://flipacoinapi.com/txt")
    result = r.text
    msg = result.encode()
    conn.write(msg)