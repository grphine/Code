
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x
from datetime import datetime
import time

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 868.0)
prev_packet = None
file = open((datetime.now()).strftime("%y%m%d.csv"), 'w+')
print("Start")

try:
    while True:
        packet = None
        packet = rfm9x.receive()
        if packet is not None:
            prev_packet = packet
            try: 
                now = datetime.now()
                date_time = now.strftime("%d-%m-%y %H:%M:%S")
                timestamp = str(time.time())

                packet_text = (str(prev_packet, "utf-8")).rstrip('\x00')
                text = (timestamp + "," + date_time + "," + packet_text)

            except Exception as e:
                print(date_time)
                print(e)
                print("data" + str(prev_packet))
            print(text, file=file, flush=True)
except KeyboardInterrupt:
    print("\nTerminating")
    file.close()
    raise SystemExit
        

