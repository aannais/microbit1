from microbit import *

while True:
    message = uart.read()

    if message:
        display.scroll(message)



